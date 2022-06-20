import { HttpClient } from '@angular/common/http';
import { Component, Input, OnInit } from '@angular/core';
import { Observable, of } from 'rxjs';
import { catchError, map } from 'rxjs/operators';

@Component({
  selector: 'app-game-map',
  templateUrl: './game-map.component.html',
  styleUrls: ['./game-map.component.scss']
})
export class GameMapComponent {

  apiLoaded: Observable<boolean>;

  @Input() gameMapOptions: google.maps.MapOptions;

  constructor(private httpClient: HttpClient) { 
    this.apiLoaded = httpClient.jsonp('https://maps.googleapis.com/maps/api/js', 'callback')
        .pipe(
          map(() => true),
          catchError(() => of(false)),
        );
  }

}
