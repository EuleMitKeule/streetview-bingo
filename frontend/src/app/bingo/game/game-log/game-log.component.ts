import { Component, OnInit } from '@angular/core';
import { User } from 'generated/openapi';
import { SocketService } from 'src/app/_shared/socket.service';
import { MessageType } from './message-type';

@Component({
  selector: 'app-game-log',
  templateUrl: './game-log.component.html',
  styleUrls: ['./game-log.component.scss']
})
export class GameLogComponent implements OnInit {

  constructor(private socketService: SocketService) { }

  public gameLog: [MessageType, any][] = [];

  ngOnInit(): void {

    this.socketService.socket.on("game_chat_message", data => {
      this.onGameChatMessage(data);
    })
  }

  onGameChatMessage(data: any) {
    let messageType = MessageType[data.messageType];
    let messageData = data.messageData;
    
    console.log(`got message with type ${messageType} and data ${messageData}`);
    
    this.gameLog.push([messageType, messageData]);
  }
}
