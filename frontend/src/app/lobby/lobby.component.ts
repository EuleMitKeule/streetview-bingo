import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { Lobby, LobbyService } from 'generated/openapi';
import { Socket } from 'ngx-socket-io';
import { Observable } from 'rxjs';
import { LoginService } from '../_shared/login.service';

@Component({
  selector: 'app-lobby',
  templateUrl: './lobby.component.html',
  styleUrls: ['./lobby.component.css']
})
export class LobbyComponent implements OnInit {

  constructor(private loginService: LoginService, private lobbyService: LobbyService, private route: ActivatedRoute, private socket: Socket) { }

  userToken: string = "";
  userId: number = this.loginService.userId;
  lobbyToken: string = "";

  lobby: Lobby;

  ngOnInit(): void {
    this.userToken = this.loginService.userToken;

    this.route.params.subscribe(params => {
      this.lobbyToken = params.token;
      this.loadLobby();
      this.socket.emit("join", this.lobbyToken);
    })

    this.socket.on("reload", x => {
      console.log("Reloading");
      this.loadLobby();
    });

  }

  loadLobby() {
    this.lobbyService.apiGetLobby(this.lobbyToken, this.userToken).subscribe(x => {
      this.lobby = x;
    })
  }

  copyToken(){
    const selBox = document.createElement('textarea');
    selBox.style.position = 'fixed';
    selBox.style.left = '0';
    selBox.style.top = '0';
    selBox.style.opacity = '0';
    selBox.value = this.lobbyToken;
    document.body.appendChild(selBox);
    selBox.focus();
    selBox.select();
    document.execCommand('copy');
    document.body.removeChild(selBox);
  }

}
