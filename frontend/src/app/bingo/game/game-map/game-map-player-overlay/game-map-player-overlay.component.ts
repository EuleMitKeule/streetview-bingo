import { Component, EventEmitter, Input, Output } from '@angular/core';
import { Lobby, User, Word } from 'generated/openapi';

@Component({
  selector: 'app-game-map-player-overlay',
  templateUrl: './game-map-player-overlay.component.html',
  styleUrls: ['./game-map-player-overlay.component.scss']
})
export class GameMapPlayerOverlayComponent {

  constructor() { }
  
  @Input() currentUser: User;
  @Input() currentLobby: Lobby;

  @Output() wordClick: EventEmitter<Word> = new EventEmitter();

  get remainingWords(): Word[] {
    return this.currentLobby.words.filter(w => !w.users.some(u => u.id === this.currentUser.id));
  }

  onWordClick(word: Word): void {
    this.wordClick.emit(word);
  }
}
