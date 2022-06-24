import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { User } from 'generated/openapi';
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
export class LoginComponent implements OnInit {

  constructor(private route: ActivatedRoute,private socketService: SocketService, private joinService: JoinService, private lobbiesService: LobbiesService, private usersService: UsersService, private loginService: LoginService, private router: Router) {}
  
  username: string = "";
  lobbyToken: string = "";
  
  public activeNavId: number;
    
  ngOnInit(): void {
    this.route.params.subscribe(params => {
      this.lobbyToken = params.token;
      this.activeNavId = this.lobbyToken !== "" ? 2 : 1;
    });
  }

  onCreateLobbyFormSubmit(user: User): void {
    this.lobbiesService.createLobby({
      "owner": user,
      "users": [user],
    }).subscribe(lobby => {
      this.router.navigate(['lobby', lobby.token])
    });
  }

  onJoinLobbyFormSubmit(user: User): void {
    this.joinService.joinLobby(
      this.lobbyToken, 
      user
    ).subscribe(lobby => {
      this.socketService.socket.emit("reload", {
        room: lobby.token
      });
      this.router.navigate(['lobby', lobby.token])
    })
  }
}
