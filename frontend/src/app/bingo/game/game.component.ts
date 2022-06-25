import { Component, EventEmitter, Input, OnInit, Output } from '@angular/core';
import { Lobby, User, Word } from 'generated/openapi';
import { SocketService } from 'src/app/_shared/socket.service';

@Component({
  selector: 'app-game',
  templateUrl: './game.component.html',
  styleUrls: ['./game.component.scss']
})
export class GameComponent implements OnInit {

  constructor(private socketService: SocketService) { }
  
  @Input() currentLobby: Lobby;
  @Input() currentUser: User;
  
  @Output() gameLobbyUpdate: EventEmitter<Lobby> = new EventEmitter();
  @Output() gameWordUpdate: EventEmitter<Word> = new EventEmitter();
  
  
  get isReviewing(): boolean {
    return this.usersToReview.length > 0;
  }
  followedUser: User;
  usersToReview: [User, Word][] = [];

  ngOnInit(): void {
    if (this.currentLobby.moderator.id === this.currentUser.id) {
      this.socketService.socket.on("game_word_found", data => {
        this.onGameWordFound(data.user, data.word);
      });
    }
  }

  getReviewedUser(): User {
    return this.usersToReview.length > 0 ? this.usersToReview[0][0] : null;
  }

  getViewedUser(): User {
    let reviewedUser: User = this.getReviewedUser();

    if (reviewedUser) {
      return reviewedUser;
    }
    return this.followedUser;
  }

  onFollowUser(user: User): void {
    this.followedUser = user;
  }

  onGameWordFound(user: User, word: Word): void {
    this.usersToReview = this.usersToReview.filter(x => x[0].id !== user.id);
    this.usersToReview.push([user, word]);
  }

  onAcceptClick(): void {
    let [user, word]: [User, Word] = this.usersToReview.shift();

    word.users.push(user);
    this.gameWordUpdate.emit(word);
    this.emitGameWordFoundMessage(user, word);
  }

  onRejectClick(): void {
    let [user, word]: [User, Word] = this.usersToReview.shift();
    
    this.emitGameWordRejectedMessage(user, word);
    //TODO: send reject to user
  }

  onWordClick(word: Word): void {
    this.emitGameWordFound(word);
  }

  emitGameWordFound(word: Word): void {
    this.socketService.socket.emit("game_word_found", {
      room: this.currentLobby.token,
      user: this.currentUser,
      word: word
    });
  }

  emitGameWordFoundMessage(user: User, word: Word): void {
    console.log(`emitting game word found message for user ${user.name} and word ${word.text}`);

    this.socketService.socket.emit("game_chat_message", {
      room: this.currentLobby.token,
      messageType: "WordAcceptedMessage",
      messageData: {
        user: user,
        word: word
      }
    });
  }

  emitGameWordRejectedMessage(user: User, word: Word): void {
    console.log(`emitting game word rejected message for user ${user.name} and word ${word.text}`);

    this.socketService.socket.emit("game_chat_message", {
      room: this.currentLobby.token,
      messageType: "WordRejectedMessage",
      messageData: {
        user: user,
        word: word
      }
    });
  }
}
