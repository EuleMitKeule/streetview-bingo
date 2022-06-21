import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { JoinService } from 'generated/openapi/api/join.service';
import { LobbiesService } from 'generated/openapi/api/lobbies.service';
import { UsersService } from 'generated/openapi/api/users.service';
import { Socket } from 'ngx-socket-io';
import { LoginService } from '../_shared/login.service';
import { SocketService } from '../_shared/socket.service';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.scss']
})
export class LoginComponent {

  constructor(private socketService: SocketService, private joinService: JoinService, private lobbiesService: LobbiesService, private usersService: UsersService, private loginService: LoginService, private router: Router) {}
  
  username: string = "";
  lobbyToken: string = "";

  socket: Socket = this.socketService.socket;

  createLobby() {
    this.usersService.createUser({
      "name": this.username
    }).subscribe(user => {
      this.loginService.setUser(user);

      this.lobbiesService.createLobby({
        "owner": this.loginService.user,
        "users": [this.loginService.user],
      }).subscribe(lobby => {
        this.router.navigate(['lobby', lobby.token])
      });
    });
  }

  joinLobby() {
    this.usersService.createUser({
      "name": this.username
    }).subscribe(user => {
      this.loginService.setUser(user);
      this.joinService.joinLobby(
        this.lobbyToken, 
        this.loginService.user
      ).subscribe(lobby => {
        this.socket.emit("reload", {
          room: lobby.token
        });
        this.router.navigate(['lobby', lobby.token])
      })
    });
  }
}
