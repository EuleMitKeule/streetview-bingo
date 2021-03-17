import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { LobbyService } from 'generated/openapi';
import { Socket } from 'ngx-socket-io';
import { LoginService } from '../_shared/login.service';
import { map } from 'rxjs/operators';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {

  username: string = "";
  lobbyToken: string = "";
  userToken: string = "";

  constructor(private lobbyService: LobbyService, private loginService: LoginService, private router: Router, private socket: Socket) {}

  ngOnInit(): void {
  }

  createLobby() {
    this.lobbyService.apiCreateLobby({"username": this.username }).subscribe(x => {
      this.loginService.setUserToken(x.user.token);
      this.loginService.setUserId(x.user.id)
      this.router.navigate(['lobby', x.lobby.token])
    });

  }

  joinLobby() {
    this.lobbyService.apiJoinLobby(this.lobbyToken, {"username": this.username}).subscribe(x => {
      this.loginService.setUserToken(x.token);
      this.loginService.setUserId(x.id)
      this.router.navigate(['lobby', this.lobbyToken])
    })
  }

}
