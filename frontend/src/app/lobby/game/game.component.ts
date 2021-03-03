import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { Game, GameService, GameWord } from 'generated/openapi';
import { Observable } from 'rxjs';
import { LoginService } from 'src/app/_shared/login.service';

@Component({
  selector: 'app-game',
  templateUrl: './game.component.html',
  styleUrls: ['./game.component.css']
})
export class GameComponent implements OnInit {

  constructor(private gameService: GameService, private route: ActivatedRoute, private loginService: LoginService) { }

  game$: Observable<Game>;

  gameToken: string = ""
  lobbyToken: string = ""
  userToken: string = this.loginService.userToken;
  userId: number = this.loginService.userId;

  wordInput: string = "";

  game: Game;

  ngOnInit(): void {
    this.route.params.subscribe(params => {
      this.gameToken = params.gameToken;
      this.lobbyToken = params.lobbyToken;
      this.game$ = this.gameService.apiGetGame(this.lobbyToken, this.gameToken)
      this.gameService.apiGetGame(this.lobbyToken, this.gameToken).subscribe(game => {
        this.game = game;
      })
    })

  }

  addWord() {

    let newWord: GameWord = {
      text: this.wordInput,
      users: []
    }

    this.wordInput = "";

    this.game.words.push(newWord)

    this.gameService.apiUpdateGame(this.lobbyToken, this.gameToken, this.userToken, this.game).subscribe(x => {
      console.log(x);
    });
  }

  removeWord(word: GameWord) {
    this.game.words = this.game.words.filter(item => item !== word);
    this.gameService.apiUpdateGame(this.lobbyToken, this.gameToken, this.userToken, this.game).subscribe(x => {
      console.log(x);
    });
  }

  startGame() {
    this.game.status = "started";
    this.gameService.apiUpdateGame(this.lobbyToken, this.gameToken, this.userToken, this.game).subscribe(x => {
      console.log(x);
    });
  }

  

}
