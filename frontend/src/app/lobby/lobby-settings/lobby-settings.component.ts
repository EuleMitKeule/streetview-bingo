import { Component, Input, OnInit } from '@angular/core';
import { LobbiesService, Lobby, User, UsersService, Word, WordsService } from 'generated/openapi';
import { LoginService } from 'src/app/_shared/login.service';

@Component({
  selector: 'app-lobby-settings',
  templateUrl: './lobby-settings.component.html',
  styleUrls: ['./lobby-settings.component.scss']
})
export class LobbySettingsComponent implements OnInit {

  constructor(private wordsService: WordsService, private usersService: UsersService, private lobbiesService: LobbiesService, private loginService: LoginService) { }

  @Input() lobby: Lobby;
  @Input() user: User;

  ngOnInit(): void {
  }

  onModeratorFormSubmit(userId: number): void {
    this.usersService.readUser(userId).subscribe(user => {  
      this.lobby.moderator = user;
      this.lobby.state = "words";
      this.lobbiesService.updateLobby(this.lobby.id, this.lobby).subscribe(lobby => {
        this.loginService.setLobby(lobby);
      });
    });
  }

  onAddWord(text: string): void {
    this.wordsService.createWord({
      text: text
    }).subscribe(word => {
      this.lobby.words.push(word);
      this.lobbiesService.updateLobby(this.lobby.id, this.lobby).subscribe(lobby => {
        this.loginService.setLobby(lobby);
      });
    });

  }

  onRemoveWord(word: Word): void {
    console.log(this.lobby.words);
    this.lobby.words = this.lobby.words.filter(w => w.id !== word.id);
    console.log(this.lobby.words);
    this.lobbiesService.updateLobby(this.lobby.id, this.lobby).subscribe(lobby => {
      this.loginService.setLobby(lobby);
    });
  }

  onWordsFormSubmit(): void {
    console.log("OIASJDOIAJSDio")
    this.lobby.state = "game";
    this.lobbiesService.updateLobby(this.lobby.id, this.lobby).subscribe(lobby => {
      this.loginService.setLobby(lobby);
    });
  }
}
