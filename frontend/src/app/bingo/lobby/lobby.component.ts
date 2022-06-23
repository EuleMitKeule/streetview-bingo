import { Component, EventEmitter, Input, OnInit, Output } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { LobbiesService, Lobby, User } from 'generated/openapi';
import { LobbiesByTokenService } from 'generated/openapi/api/lobbiesByToken.service';
import { LoginService } from '../../_shared/login.service';
import { SocketService } from '../../_shared/socket.service';

@Component({
  selector: 'app-lobby',
  templateUrl: './lobby.component.html',
  styleUrls: ['./lobby.component.scss']
})
export class LobbyComponent {

  constructor() { }

  @Input() currentLobby: Lobby;
  @Input() currentUser: User;
  @Input() setLobby: (lobby: Lobby) => void;

  @Output() lobbyUpdate: EventEmitter<Lobby> = new EventEmitter<Lobby>();

  onLobbySettingsUpdate(lobby: Lobby) {
    this.lobbyUpdate.emit(lobby);
  }
}
