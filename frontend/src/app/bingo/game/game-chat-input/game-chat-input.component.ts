import { Component, Input, OnInit } from '@angular/core';
import { Lobby, User } from 'generated/openapi';
import { SocketService } from 'src/app/_shared/socket.service';
import { MessageType } from '../game-log/message-type';

@Component({
  selector: 'app-game-chat-input',
  templateUrl: './game-chat-input.component.html',
  styleUrls: ['./game-chat-input.component.scss']
})
export class GameChatInputComponent {

  constructor(private socketService: SocketService) { }

  @Input() currentUser: User;
  @Input() currentLobby: Lobby;

  public message: string;

  onClick() {
    if (!this.message) {
      return;
    }

    this.socketService.socket.emit("game_chat_message", {
      room: this.currentLobby.token,
      messageType: MessageType.ChatMessage,
      messageData: {
        user: this.currentUser,
        message: this.message
      }
    });
  }
}
