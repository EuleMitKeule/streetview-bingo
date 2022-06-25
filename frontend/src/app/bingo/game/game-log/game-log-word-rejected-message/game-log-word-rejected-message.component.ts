import { Component, Input, OnInit } from '@angular/core';
import { User, Word } from 'generated/openapi';

@Component({
  selector: 'app-game-log-word-rejected-message',
  templateUrl: './game-log-word-rejected-message.component.html',
  styleUrls: ['./game-log-word-rejected-message.component.scss']
})
export class GameLogWordRejectedMessageComponent {

  constructor() { }

  @Input() user: User;
  @Input() word: Word;
}
