import { Component, Input, OnInit } from '@angular/core';
import { LobbiesService, Lobby, User } from 'generated/openapi';

@Component({
  selector: 'app-lobby-information',
  templateUrl: './lobby-information.component.html',
  styleUrls: ['./lobby-information.component.scss']
})
export class LobbyInformationComponent implements OnInit {

  constructor(private lobbiesService: LobbiesService) { }

  @Input() lobby: Lobby;
  @Input() user: User;

  ngOnInit(): void {
  }

  copyToken(): void {
    const selBox = document.createElement('textarea');
    selBox.style.position = 'fixed';
    selBox.style.left = '0';
    selBox.style.top = '0';
    selBox.style.opacity = '0';
    selBox.value = this.lobby.token;
    document.body.appendChild(selBox);
    selBox.focus();
    selBox.select();
    document.execCommand('copy');
    document.body.removeChild(selBox);
  }

  startGame(): void {
    this.lobby.state = "game";
    this.lobbiesService.updateLobby(this.lobby.id, this.lobby).subscribe()
  }

}
