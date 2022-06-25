import { Component, Input, OnInit } from '@angular/core';
import { User, Word } from 'generated/openapi';

@Component({
  selector: 'app-game-log-word-accepted-message',
  templateUrl: './game-log-word-accepted-message.component.html',
  styleUrls: ['./game-log-word-accepted-message.component.scss']
})
export class GameLogWordAcceptedMessageComponent {

  constructor() { }

  @Input() user: User;
  @Input() word: Word;

}
