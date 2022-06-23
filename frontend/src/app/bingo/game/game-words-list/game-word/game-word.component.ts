import { Component, Input, OnInit } from '@angular/core';
import { Lobby, User, Word } from 'generated/openapi';
import { faCheck, faXmark } from '@fortawesome/free-solid-svg-icons';

@Component({
  selector: 'app-game-word',
  templateUrl: './game-word.component.html',
  styleUrls: ['./game-word.component.scss']
})
export class GameWordComponent {

  constructor() { }

  @Input() currentUser: User;
  @Input() currentLobby: Lobby;
  @Input() word: Word;

  faCheck = faCheck;
  faXmark = faXmark;

  get isFound(): boolean {
    return this.word.users.some(x => x.id === this.currentUser.id);
  }

  get isModerator(): boolean {
    return this.currentLobby.moderator.id === this.currentUser.id;
  }
}
