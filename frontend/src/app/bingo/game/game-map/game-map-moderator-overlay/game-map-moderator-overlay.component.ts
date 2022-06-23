import { Component, EventEmitter, Input, OnInit, Output } from '@angular/core';
import { Lobby, User } from 'generated/openapi';

@Component({
  selector: 'app-game-map-moderator-overlay',
  templateUrl: './game-map-moderator-overlay.component.html',
  styleUrls: ['./game-map-moderator-overlay.component.scss']
})
export class GameMapModeratorOverlayComponent {

  constructor() { }
  
  @Input() currentUser: User;
  @Input() currentLobby: Lobby;
  @Input() viewedUser: User;
  @Input() isReviewing: boolean;

  @Output() acceptClick: EventEmitter<void> = new EventEmitter();
  @Output() rejectClick: EventEmitter<void> = new EventEmitter();
  @Output() followUser: EventEmitter<User> = new EventEmitter();

  public selectedUserId: number;

  get isModerator(): boolean {
    return this.currentUser.id === this.currentLobby.moderator.id;
  }

  get otherUsers(): User[] {
    return this.currentLobby.users.filter(u => u.id !== this.currentUser.id);
  }

  onAcceptClick(): void {
    this.acceptClick.emit();
  }

  onRejectClick(): void {
    this.rejectClick.emit();
  }

  onFollowUserClick(e): void {
    let user: User = this.otherUsers.find(u => u.id === +e.target.value);
    this.followUser.emit(user);
  }
}
