import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { Lobby, User, UsersService, Word } from 'generated/openapi';
import { LobbiesService } from 'generated/openapi/api/lobbies.service';
import { LobbiesByTokenService } from 'generated/openapi/api/lobbiesByToken.service';
import { Socket } from 'ngx-socket-io';
import { LoginService } from '../_shared/login.service';
import { SocketService } from '../_shared/socket.service';

@Component({
  selector: 'app-lobby',
  templateUrl: './lobby.component.html',
  styleUrls: ['./lobby.component.scss']
})
export class LobbyComponent implements OnInit {

  constructor(private usersService: UsersService, private loginService: LoginService, private lobbiesByTokenService: LobbiesByTokenService, private lobbiesService: LobbiesService, private route: ActivatedRoute, private socketService: SocketService, private router: Router) { }

  lobby: Lobby;
  user: User;
  lobbyToken: string;
  wordInput: string;

  selectedModeratorId: number;

  socket: Socket = this.socketService.socket;

  ngOnInit(): void {

    this.user = this.loginService.user;

    this.route.params.subscribe(params => {
      this.refreshLobby();
      
      this.socket.emit("join", { 
        room: this.loginService.lobby
      });
    });

    this.socket.on("reload", x => {
      this.refreshLobby();
    });
  }

  refreshLobby() {
    this.lobbiesByTokenService.readLobbyByToken(
      this.loginService.lobby.token
    ).subscribe(lobby => {
      this.loginService.setLobby(lobby);
      this.lobbyToken = lobby.token;
      this.lobby = lobby;
    });
  }

  startGame() {
    
  }

  backToHome() {
    this.loginService.setUser(null);
    this.loginService.setLobby(null);
    this.router.navigate(["/"]);
  }

  markFound(wordId: number, userId: number) {

  }

  markNotFound(wordId: number, userId: number) {

  }

  userFoundWord(userId: number, wordId: number) {
    return false;
  }

  addWord() {

  }

  removeWord(word: Word) {
    
  }

  startRound() {

  }

  selectModerator() {
    this.usersService.readUser(this.selectedModeratorId).subscribe(user => {
      this.lobby.moderator = user;

      this.lobbiesService.updateLobby(this.lobby.id, this.lobby).subscribe(lobby => {
        this.lobby = lobby;
      });
    });
  }
}
