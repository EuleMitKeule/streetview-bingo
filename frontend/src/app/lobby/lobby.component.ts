import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { Lobby, LobbyService } from 'generated/openapi';
import { Observable } from 'rxjs';
import { LoginService } from '../_shared/login.service';

@Component({
  selector: 'app-lobby',
  templateUrl: './lobby.component.html',
  styleUrls: ['./lobby.component.css']
})
export class LobbyComponent implements OnInit {

  constructor(private loginService: LoginService, private lobbyService: LobbyService, private route: ActivatedRoute) { }

  userToken: string = "";
  userId: number = this.loginService.userId;
  lobbyToken: string = "";

  lobby: Lobby;

  ngOnInit(): void {
    this.userToken = this.loginService.userToken;

    this.route.params.subscribe(params => {
      this.lobbyToken = params.token;
      this.loadLobby();
    })

  }

  loadLobby() {
    this.lobbyService.apiGetLobby(this.lobbyToken, this.userToken).subscribe(x => {
      this.lobby = x;
    })
  }

}
