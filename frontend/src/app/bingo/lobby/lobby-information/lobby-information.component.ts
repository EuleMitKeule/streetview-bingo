import { Component, Input, OnInit, ViewChild } from '@angular/core';
import { LobbiesService, Lobby, User } from 'generated/openapi';

@Component({
  selector: 'app-lobby-information',
  templateUrl: './lobby-information.component.html',
  styleUrls: ['./lobby-information.component.scss']
})
export class LobbyInformationComponent {

  constructor(private lobbiesService: LobbiesService) { }

  @Input() currentUser: User;
  @Input() currentLobby: Lobby;

  @ViewChild("copyButton") copyButton: any;

  get baseUrl(): string {
    return window.location.origin;
  }

  get joinUrl(): string {
    return `${this.baseUrl}/#/join/${this.currentLobby.token}`;
  }

  copyToClipboard(): void {
    navigator.clipboard.writeText(this.joinUrl).then(() => {
      this.copyButton.nativeElement.innerText = "Copied!";
    });
  }

  copyToken(): void {
    const selBox = document.createElement('textarea');
    selBox.style.position = 'fixed';
    selBox.style.left = '0';
    selBox.style.top = '0';
    selBox.style.opacity = '0';
    selBox.value = this.currentLobby.token;
    document.body.appendChild(selBox);
    selBox.focus();
    selBox.select();
    document.execCommand('copy');
    document.body.removeChild(selBox);
  }
}
