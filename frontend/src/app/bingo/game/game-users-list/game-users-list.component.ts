import { Component, EventEmitter, Input, OnInit, Output } from '@angular/core';
import { Lobby, User } from 'generated/openapi';
import { Socket } from 'ngx-socket-io';
import { SocketService } from 'src/app/_shared/socket.service';
import { faEye } from '@fortawesome/free-solid-svg-icons';

@Component({
  selector: 'app-game-users-list',
  templateUrl: './game-users-list.component.html',
  styleUrls: ['./game-users-list.component.scss']
})
export class GameUsersListComponent {

  constructor() { }

  @Input() currentUser: User;
  @Input() currentLobby: Lobby;
  @Input() followedUser: User;
  @Input() userFoundWord;
  
  @Output() followUser: EventEmitter<User> = new EventEmitter<User>();

  users: User[];
  faEye = faEye;

  onFollowUser(user: User): void {
    if (this.followedUser === user) {
      this.followUser.emit(null);
    } else {
      this.followUser.emit(user);
    }
  }
}
