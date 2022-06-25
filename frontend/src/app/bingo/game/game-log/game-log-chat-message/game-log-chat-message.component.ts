import { Component, Input, OnInit } from '@angular/core';
import { User } from 'generated/openapi';

@Component({
  selector: 'app-game-log-chat-message',
  templateUrl: './game-log-chat-message.component.html',
  styleUrls: ['./game-log-chat-message.component.scss']
})
export class GameLogChatMessageComponent {

  constructor() { }

  @Input() user: User;
  @Input() message: string;
}
