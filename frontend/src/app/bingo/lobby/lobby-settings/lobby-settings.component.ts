import { Component, EventEmitter, Input, OnInit, Output } from '@angular/core';
import { LobbiesService, Lobby, User, UsersService, Word, WordsService } from 'generated/openapi';
import { Socket } from 'ngx-socket-io';
import { LoginService } from 'src/app/_shared/login.service';
import { SocketService } from 'src/app/_shared/socket.service';

@Component({
  selector: 'app-lobby-settings',
  templateUrl: './lobby-settings.component.html',
  styleUrls: ['./lobby-settings.component.scss']
})
export class LobbySettingsComponent {

  constructor(private socketService: SocketService, private wordsService: WordsService, private usersService: UsersService, private lobbiesService: LobbiesService, private loginService: LoginService) { }

  @Input() currentUser: User;
  @Input() currentLobby: Lobby;
  @Input() setLobby: (lobby: Lobby) => void;

  @Output() lobbySettingsUpdate: EventEmitter<Lobby> = new EventEmitter<Lobby>();
  
  socket: Socket = this.socketService.socket;

  onModeratorFormSubmit(selectedModeratorId: number): void {
    this.usersService.readUser(selectedModeratorId).subscribe(user => {
      this.currentLobby.moderator = user;
      this.currentLobby.lobby_state = "words";
      this.lobbySettingsUpdate.emit(this.currentLobby);
    });
  }

  onAddWord(text: string): void {
    this.wordsService.createWord({
      text: text
    }).subscribe(word => {
      this.currentLobby.words.push(word);
      this.lobbySettingsUpdate.emit(this.currentLobby);
    });
  }

  onRemoveWord(word: Word): void {
    this.currentLobby.words = this.currentLobby.words.filter(w => w.id !== word.id);
    this.lobbySettingsUpdate.emit(this.currentLobby);
  }

  onWordsFormSubmit(): void {
    this.currentLobby.state = "game";
    this.lobbySettingsUpdate.emit(this.currentLobby);
  }

  onWordsFormBack(): void {
    this.currentLobby.lobby_state = "moderator";
    this.lobbySettingsUpdate.emit(this.currentLobby);
  }
}
