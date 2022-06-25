import { Component, Input, OnInit } from '@angular/core';
import { faCheck, faXmark } from '@fortawesome/free-solid-svg-icons';
import { User, Word } from 'generated/openapi';

@Component({
  selector: 'app-word-badge',
  templateUrl: './word-badge.component.html',
  styleUrls: ['./word-badge.component.scss']
})
export class WordBadgeComponent {

  constructor() { }
  
  @Input() currentUser: User;
  @Input() word: Word;
  @Input() displayFound: boolean;

  faCheck = faCheck;
  faXmark = faXmark;

  get isFound(): boolean {
    return this.word?.users.includes(this.currentUser);
  }
}
