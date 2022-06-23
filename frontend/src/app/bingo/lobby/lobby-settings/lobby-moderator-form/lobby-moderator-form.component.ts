import { Component, EventEmitter, Input, OnInit, Output } from '@angular/core';
import { Lobby, User } from 'generated/openapi';
import { Socket } from 'ngx-socket-io';
import { SocketService } from 'src/app/_shared/socket.service';


@Component({
  selector: 'app-lobby-moderator-form',
  templateUrl: './lobby-moderator-form.component.html',
  styleUrls: ['./lobby-moderator-form.component.scss']
})
export class LobbyModeratorFormComponent implements OnInit {

  constructor(private socketService: SocketService) { }

  @Input() currentLobby: Lobby;
  @Input() currentUser: User;

  private _selectedModeratorId: number;

  set selectedModeratorId(value: number) {
    this._selectedModeratorId = value;
    
    if (this.currentLobby.owner.id === this.currentUser.id) {
      this.socket.emit("lobby_moderator_update", {
        selectedModeratorId: this.selectedModeratorId,
        room: this.currentLobby.token
      });
    }
  }

  get selectedModeratorId(): number {
    return this._selectedModeratorId;
  }
  
  socket: Socket = this.socketService.socket;

  @Output() moderatorFormSubmit: EventEmitter<number> = new EventEmitter<number>();

  ngOnInit(): void {
    if (this.currentLobby.owner.id !== this.currentUser.id) {
      this.socket.on("lobby_moderator_update", (data) => {
        this.onLobbyModeratorUpdate(data);
      });
    }
  }

  onLobbyModeratorUpdate(data: any): void {
    this.selectedModeratorId = data.selectedModeratorId;
  }

  onSubmit(): void {
    this.moderatorFormSubmit.emit(this.selectedModeratorId);
  }
}
