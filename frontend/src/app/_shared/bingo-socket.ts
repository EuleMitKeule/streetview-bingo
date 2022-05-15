import { Injectable } from "@angular/core";
import { Socket } from "ngx-socket-io";
import { ConfigurationService } from "./configuration.service";

@Injectable()
export class BingoSocket extends Socket {
    constructor() {
        super({url: "https://bingo.eulenet.eu", options: {}});
    }
}
