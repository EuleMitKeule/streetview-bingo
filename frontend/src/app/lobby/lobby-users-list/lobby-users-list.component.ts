import { Component, Input, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { Lobby } from 'generated/openapi';
import { LoginService } from 'src/app/_shared/login.service';

@Component({
  selector: 'app-lobby-users-list',
  templateUrl: './lobby-users-list.component.html',
  styleUrls: ['./lobby-users-list.component.scss']
})
export class LobbyUsersListComponent {

  constructor() { }

  @Input() lobby: Lobby;

}
