import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { LobbiesByTokenService, LobbiesService, Lobby, User, Word, WordsService } from 'generated/openapi';
import { LoginService } from '../_shared/login.service';
import { SocketService } from '../_shared/socket.service';

@Component({
  selector: 'app-bingo',
  templateUrl: './bingo.component.html',
  styleUrls: ['./bingo.component.scss']
})
export class BingoComponent implements OnInit {

  constructor(
    private loginService: LoginService, 
    private lobbiesService: LobbiesService,
    private lobbiesByTokenService: LobbiesByTokenService,
    private wordsService: WordsService,
    private route: ActivatedRoute, 
    private socketService: SocketService, 
    private router: Router
  ) { }

  currentLobby: Lobby;
  currentUser: User;

  ngOnInit(): void {

    if (!this.loginService.user) {
      this.router.navigate(['/']);
    }

    this.currentUser = this.loginService.user;
    this.refreshLobby();

    this.socketService.socket.on("reload", data => {
      this.refreshLobby();
    });
  }
  
  refreshLobby() {
    this.route.params.subscribe(params => {
      this.lobbiesByTokenService.readLobbyByToken(
        params.token
      ).subscribe(lobby => {
        if (!lobby.users.includes(this.currentUser)) {
          if (lobby?.state === "lobby" && lobby?.lobby_state === "moderator") {
            // Navigate to join page with token
          } else {
            this.router.navigate(['/']);
          }
        }

        this.currentLobby = lobby;
        this.emitJoin(lobby);
      });
    });
  }

  emitJoin(lobby: Lobby) {
    this.socketService.socket.emit("join", { 
      room: lobby.token
    });
  }

  onLobbyUpdate(lobby: Lobby) {
    this.lobbiesService.updateLobby(
      lobby.id,
      lobby
    ).subscribe(lobby => {
      this.currentLobby = lobby;
      this.socketService.socket.emit("reload", {
        room: this.currentLobby.token
      });
    });
  }

  onWordUpdate(word: Word) {
    this.wordsService.updateWord(
      word.id,
      word
    ).subscribe(word => {
      this.refreshLobby();
      this.socketService.socket.emit("reload", {
        room: this.currentLobby.token
      });
    });
  }
}

