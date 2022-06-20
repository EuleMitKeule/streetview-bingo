import { Component, Input, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { Lobby } from 'generated/openapi';

@Component({
  selector: 'app-lobby-information-form',
  templateUrl: './lobby-information-form.component.html',
  styleUrls: ['./lobby-information-form.component.scss']
})
export class LobbyInformationFormComponent implements OnInit {

  constructor() { }

  @Input() lobby: Lobby;

  public selectedModeratorId: number;

  ngOnInit(): void {
  }

  selectModerator(): void {

  }

}
