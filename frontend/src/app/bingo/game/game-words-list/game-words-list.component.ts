import { Component, Input, OnInit } from '@angular/core';
import { Lobby, User, Word } from 'generated/openapi';
import { Socket } from 'ngx-socket-io';
import { SocketService } from 'src/app/_shared/socket.service';

@Component({
  selector: 'app-game-words-list',
  templateUrl: './game-words-list.component.html',
  styleUrls: ['./game-words-list.component.scss']
})
export class GameWordsListComponent {

  constructor(private socketService: SocketService) { }

  @Input() currentLobby: Lobby;
  @Input() currentUser: User;
  
  onWordFound(word: Word): void {
    if (this.currentLobby.moderator.id === this.currentUser.id) {
      return;
    }

    this.socketService.socket.emit("game_word_found", {
      room: this.currentLobby.token,
      user: this.currentUser,
      word: word
    })
  }
}
