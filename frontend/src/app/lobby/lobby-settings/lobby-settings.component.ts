import { Component, Input, OnInit } from '@angular/core';
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

  @Input() lobby: Lobby;
  @Input() setLobby: (lobby: Lobby) => void;
  @Input() user: User;
  
  socket: Socket = this.socketService.socket;

  onModeratorFormSubmit(selectedModeratorId: number): void {
    this.usersService.readUser(selectedModeratorId).subscribe(user => {
      this.lobby.moderator = user;
      this.lobby.state = "words";
      this.lobbiesService.updateLobby(this.lobby.id, this.lobby).subscribe(lobby => {
        this.setLobby(lobby);
        this.socket.emit("reload", {
          room: this.lobby.token
        });
      });
    });
  }

  onAddWord(text: string): void {
    this.wordsService.createWord({
      text: text
    }).subscribe(word => {
      this.lobby.words.push(word);
      this.lobbiesService.updateLobby(this.lobby.id, this.lobby).subscribe(lobby => {
        this.setLobby(lobby);
        this.socket.emit("reload", {
          room: this.lobby.token
        });
      });
    });
  }

  onRemoveWord(word: Word): void {
    this.lobby.words = this.lobby.words.filter(w => w.id !== word.id);
    this.lobbiesService.updateLobby(this.lobby.id, this.lobby).subscribe(lobby => {
      this.setLobby(lobby);
      this.socket.emit("reload", {
        room: this.lobby.token
      });
    });
  }

  onWordsFormSubmit(): void {
    this.lobby.state = "game";
    this.lobbiesService.updateLobby(this.lobby.id, this.lobby).subscribe(lobby => {
      this.setLobby(lobby);
    });
  }
}
