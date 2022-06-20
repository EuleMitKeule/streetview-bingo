import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { Word } from 'generated/openapi';
import { Socket } from 'ngx-socket-io';
import { LoginService } from 'src/app/_shared/login.service';
import { SocketService } from 'src/app/_shared/socket.service';

@Component({
  selector: 'app-game',
  templateUrl: './game.component.html',
  styleUrls: ['./game.component.scss']
})
export class GameComponent implements OnInit {

  constructor(private route: ActivatedRoute, private loginService: LoginService, private socketService: SocketService) { }

  // //game$: Observable<Game>;

  // lobbyToken: string = "";
  // wordInput: string = "";

  // socket: Socket = this.socketService.socket;

  ngOnInit(): void {
    // this.route.params.subscribe(params => {
    //   this.lobbyToken = params.lobbyToken;
    //   this.loadGame();

    //   this.socket.on("reload", x => {
    //     console.log("Reloading");
    //     this.loadGame();
    //   });
    // })
  }

  // loadGame() {
    
  // }


  // addWord() {

  //   let newWord: Word = {
  //     text: this.wordInput
  //   }

  //   this.wordInput = "";

  //   this.lobby.words.push(newWord)

  //   this.gameService.apiUpdateGame(this.lobbyToken, this.gameToken, this.userToken, this.game).subscribe(x => {
  //     console.log(x);
  //   });
  // }

  // removeWord(word: GameWord) {
  //   this.game.words = this.game.words.filter(item => item !== word);
  //   this.gameService.apiUpdateGame(this.lobbyToken, this.gameToken, this.userToken, this.game).subscribe(x => {
  //     console.log(x);
  //   });
  // }

  // startGame() {
  //   this.game.status = "started";
  //   this.gameService.apiUpdateGame(this.lobbyToken, this.gameToken, this.userToken, this.game).subscribe(x => {
  //     console.log(x);
  //     this.loadGame();
  //   });
  // }

  // markFound(wordId: number, userId: number) {
  //   console.log(this.game)
  //   this.gameService.apiCreateWordStatus(this.lobbyToken, this.gameToken, wordId, userId, this.userToken).subscribe(x => {
  //     console.log(x);
  //     this.game.words.filter(word => word.id == wordId)[0].users.push({id: userId})
  //   })
  // }

  // markNotFound(wordId: number, userId: number) {
  //   this.gameService.apiDeleteWordStatus(this.lobbyToken, this.gameToken, wordId, userId, this.userToken).subscribe(x => {
  //     console.log(x);
  //     let word = this.game.words.filter(word => word.id == wordId)[0];
  //     word.users = word.users.filter(user => user.id != userId)
  //   })
  // }

  // userFoundWord(userId: number, wordId: number) {
  //   let found_word = this.game.words.filter(word => word.id == wordId)[0];
  //   let found_user = found_word.users.filter(user => user.id == userId);
  //   return found_user.length > 0
  // }

  

}
