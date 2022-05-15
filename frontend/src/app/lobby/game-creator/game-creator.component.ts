import { Component, Input, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { Game, GameService, Lobby, User } from 'generated/openapi';
import { LoginService } from 'src/app/_shared/login.service';

@Component({
  selector: 'app-game-creator',
  templateUrl: './game-creator.component.html',
  styleUrls: ['./game-creator.component.scss']
})
export class GameCreatorComponent implements OnInit {

  @Input() lobby: Lobby;

  selectedModeratorId: number;

  constructor(private gameService: GameService, private loginService: LoginService, private router: Router) { }

  ngOnInit(): void {
    console.log("hello")
    console.log(this.lobby);
  }

  createGame() {
    console.log("hallo world")

    let game: Game = {
      moderator: {
        id: Number(this.selectedModeratorId)
      },
      users: this.lobby.users
    }

    this.gameService.apiCreateGame(this.lobby.token, this.loginService.userToken, game).subscribe(x => {
      console.log(x);
      this.router.navigate(["lobby", this.lobby.token, "game", x.token]);
    });
  }

}
