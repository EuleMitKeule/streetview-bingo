import { Component, EventEmitter, Input, OnInit, Output } from '@angular/core';
import { Lobby, User, Word, WordsService } from 'generated/openapi';

@Component({
  selector: 'app-lobby-words-form',
  templateUrl: './lobby-words-form.component.html',
  styleUrls: ['./lobby-words-form.component.scss']
})
export class LobbyWordsFormComponent implements OnInit {

  constructor(private wordsService: WordsService) { }

  @Input() words: Word[];
  @Input() isModerator: boolean;
  @Output() onAddWord: EventEmitter<string> = new EventEmitter<string>();
  @Output() onRemoveWord: EventEmitter<Word> = new EventEmitter<Word>();
  @Output() onWordsFormSubmit: EventEmitter<void> = new EventEmitter<void>();

  public wordInput: string;

  ngOnInit(): void {
  }

  addWord(): void {
    this.onAddWord.emit(this.wordInput);
  }

  removeWord(word: Word): void {
    this.onRemoveWord.emit(word);
  }

  onSubmit(): void {
    this.onWordsFormSubmit.emit();
  }
}
