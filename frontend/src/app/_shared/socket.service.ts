import { Injectable } from '@angular/core';
import { Socket } from 'ngx-socket-io';
import { ConfigurationService } from './configuration.service';

@Injectable({
  providedIn: 'root'
})
export class SocketService {

  public socket?: Socket;

  constructor(configurationService: ConfigurationService) {
    let url: string = configurationService.getConfig().SOCKET_BASE_PATH;
    this.socket = new Socket({
      url: url
    })
  }

}
