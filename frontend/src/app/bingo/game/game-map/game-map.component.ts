import { HttpClient } from '@angular/common/http';
import { Component, EventEmitter, Input, OnInit, Output } from '@angular/core';
import { Lobby, User, Word } from 'generated/openapi';
import { Observable, of } from 'rxjs';
import { catchError, map } from 'rxjs/operators';
import { SocketService } from 'src/app/_shared/socket.service';

@Component({
  selector: 'app-game-map',
  templateUrl: './game-map.component.html',
  styleUrls: ['./game-map.component.scss']
})
export class GameMapComponent implements OnInit {
  
  constructor(private socketService: SocketService, private httpClient: HttpClient) { 
    this.apiLoaded = httpClient.jsonp(
      'https://maps.googleapis.com/maps/api/js?', 
      'callback'
    ).pipe(
      map(() => true),
      catchError(() => of(false)),
    );
  }

  @Input() currentUser: User;
  @Input() currentLobby: Lobby;
  @Input() viewedUser: User;
  @Input() isReviewing: boolean;

  @Output() acceptClick: EventEmitter<void> = new EventEmitter();
  @Output() rejectClick: EventEmitter<void> = new EventEmitter();
  @Output() followUser: EventEmitter<User> = new EventEmitter();
  @Output() wordClick: EventEmitter<Word> = new EventEmitter();

  googleMap: google.maps.Map;
  gameMapOptions: google.maps.MapOptions = {
    streetViewControlOptions: {
    },
    streetViewControl: true,
    center: { lat: 40, lng: -20 },
    zoom: 4,
  };  
  apiLoaded: Observable<boolean>;

  get isModerator(): boolean {
    return this.currentUser.id === this.currentLobby.moderator.id;
  }
  
  ngOnInit(): void {

    this.socketService.socket.on("game_map_sync", data => {
      this.onGameMapSync(data);
    });
  }

  onMapInitialized(map: google.maps.Map) {
    this.googleMap = map;
    this.subscribeEvents();
  }

  subscribeEvents(): void {      
    this.googleMap.getStreetView().addListener("visible_changed", () => {
      this.syncMap();
    });

    this.googleMap.getStreetView().addListener("position_changed", () => {
      this.syncMap();
    });

    this.googleMap.getStreetView().addListener("zoom_changed", () => {
      this.syncMap();
    });

    this.googleMap.getStreetView().addListener("pov_changed", () => {
      this.syncMap();
    });

    this.googleMap.addListener("center_changed", () => {
      this.syncMap();
    });
    
    this.googleMap.addListener("zoom_changed", () => {
      this.syncMap();
    });
  }

  syncMap(): void {
    let center = this.googleMap.getCenter();
    let zoom = this.googleMap.getZoom();
    let streetViewVisible = this.googleMap.getStreetView().getVisible();
    let streetViewPosition = this.googleMap.getStreetView().getPosition();
    let streetViewZoom = this.googleMap.getStreetView().getZoom();
    let streetViewPov = this.googleMap.getStreetView().getPov();

    if (this.currentUser.id !== this.currentLobby.moderator.id) {
      let data = {
        room: this.currentLobby.token,
        user: this.currentUser,
        center: center,
        zoom: zoom,
        streetViewVisible: streetViewVisible,
        streetViewPosition: streetViewPosition,
        streetViewZoom: streetViewZoom,
        streetViewPov: streetViewPov,
      }

      this.socketService.socket.emit("game_map_sync", data);
    }
  }
  
  onGameMapSync(data: any): void {
    if (data?.user?.id === this.viewedUser?.id) {
      this.googleMap.setCenter(data.center);
      this.googleMap.setZoom(data.zoom);
      this.googleMap.getStreetView().setVisible(data.streetViewVisible);
      this.googleMap.getStreetView().setPosition(data.streetViewPosition);
      this.googleMap.getStreetView().setZoom(data.streetViewZoom);
      this.googleMap.getStreetView().setPov(data.streetViewPov);
    }
  }

  onAcceptClick() {
    this.acceptClick.emit();
  }

  onRejectClick() {
    this.rejectClick.emit();
  }

  onFollowUser(user: User) {
    this.followUser.emit(user);
  }

  onWordClick(word: Word) {
    this.wordClick.emit(word);
  }
}
