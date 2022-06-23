import { Component, Input, OnInit } from '@angular/core';
import { Lobby } from 'generated/openapi';

@Component({
  selector: 'app-lobby-users-list',
  templateUrl: './lobby-users-list.component.html',
  styleUrls: ['./lobby-users-list.component.scss']
})
export class LobbyUsersListComponent {

  constructor() { }

  @Input() currentLobby: Lobby;

}
