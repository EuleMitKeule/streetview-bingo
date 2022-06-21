import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { Lobby, User, UsersService, Word } from 'generated/openapi';
import { LobbiesService } from 'generated/openapi/api/lobbies.service';
import { LobbiesByTokenService } from 'generated/openapi/api/lobbiesByToken.service';
import { Socket } from 'ngx-socket-io';
import { LoginService } from '../_shared/login.service';
import { SocketService } from '../_shared/socket.service';

@Component({
  selector: 'app-lobby',
  templateUrl: './lobby.component.html',
  styleUrls: ['./lobby.component.scss']
})
export class LobbyComponent implements OnInit {

  constructor(private usersService: UsersService, private loginService: LoginService, private lobbiesByTokenService: LobbiesByTokenService, private lobbiesService: LobbiesService, private route: ActivatedRoute, private socketService: SocketService, private router: Router) { }

  lobby: Lobby;
  user: User;
  wordInput: string;

  public gameMapOptions: google.maps.MapOptions = {
    center: { lat: 40, lng: -20 },
    zoom: 4,
  }

  socket: Socket = this.socketService.socket;

  ngOnInit(): void {

    if (this.loginService.user == null) {
      this.router.navigate(['/']);
    }

    this.user = this.loginService.user;

    
    this.route.params.subscribe(params => {
      this.lobbiesByTokenService.readLobbyByToken(params.token).subscribe(lobby => {
        this.lobby = lobby;
        this.socket.emit("join", { 
          room: lobby.token
        });
      });
    });

    this.socket.on("reload", data => {
      this.refreshLobby();
    });

    this.socket.on("connect", data => {
      console.log("Connected");
    });
  }

  refreshLobby() {
    this.lobbiesByTokenService.readLobbyByToken(
      this.lobby.token
    ).subscribe(lobby => {
      this.lobby = lobby;
    });
  }

  backToHome() {
    this.router.navigate(["/"]);
  }

  setLobby(lobby: Lobby) {

  }
}
