import { BrowserModule } from '@angular/platform-browser';
import { APP_INITIALIZER, NgModule } from '@angular/core';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { HttpClientJsonpModule, HttpClientModule } from '@angular/common/http';
import { NgbModule } from '@ng-bootstrap/ng-bootstrap';
import { LoginComponent } from './login/login.component';
import { LobbyComponent } from './bingo/lobby/lobby.component';
import { FormsModule } from '@angular/forms';
import { BASE_PATH } from 'generated/openapi';
import { ConfigurationService } from './_shared/configuration.service';
import { SocketIoModule } from 'ngx-socket-io';
import { LobbyUsersListComponent } from './bingo/lobby/lobby-users-list/lobby-users-list.component';
import { LobbyInformationComponent } from './bingo/lobby/lobby-information/lobby-information.component';
import { LobbyModeratorFormComponent } from './bingo/lobby/lobby-settings/lobby-moderator-form/lobby-moderator-form.component';
import { MenuCardComponent } from './menu-card/menu-card.component';
import { LobbySettingsComponent } from './bingo/lobby/lobby-settings/lobby-settings.component';
import { LobbyWordsFormComponent } from './bingo/lobby/lobby-settings/lobby-words-form/lobby-words-form.component';
import { GoogleMapsModule } from '@angular/google-maps';
import { GameMapComponent } from './bingo/game/game-map/game-map.component';
import { SidebarComponent } from './sidebar/sidebar.component';
import { GameUsersListComponent } from './bingo/game/game-users-list/game-users-list.component';
import { GameWordsListComponent } from './bingo/game/game-words-list/game-words-list.component';
import { FontAwesomeModule } from '@fortawesome/angular-fontawesome';
import { GameComponent } from './bingo/game/game.component';
import { BingoComponent } from './bingo/bingo.component';
import { GameWordComponent } from './bingo/game/game-words-list/game-word/game-word.component';
import { GameMapModeratorOverlayComponent } from './bingo/game/game-map/game-map-moderator-overlay/game-map-moderator-overlay.component';
import { GameMapPlayerOverlayComponent } from './bingo/game/game-map/game-map-player-overlay/game-map-player-overlay.component';
import { LoginUserFormComponent } from './login/login-user-form/login-user-form.component';
import { GameLogComponent } from './bingo/game/game-log/game-log.component';
import { GameChatInputComponent } from './bingo/game/game-chat-input/game-chat-input.component';
import { SharedModule } from 'src/shared/shared.module';
import { GameLogChatMessageComponent } from './bingo/game/game-log/game-log-chat-message/game-log-chat-message.component';
import { GameLogUserWordMessageComponent } from './bingo/game/game-log/game-log-user-word-message/game-log-user-word-message.component';
import { GameLogWordRejectedMessageComponent } from './bingo/game/game-log/game-log-word-rejected-message/game-log-word-rejected-message.component';
import { GameLogWordAcceptedMessageComponent } from './bingo/game/game-log/game-log-word-accepted-message/game-log-word-accepted-message.component';


@NgModule({
  declarations: [
    AppComponent,
    LoginComponent,
    LobbyComponent,
    LobbyUsersListComponent,
    LobbyInformationComponent,
    LobbyModeratorFormComponent,
    MenuCardComponent,
    LobbySettingsComponent,
    LobbyWordsFormComponent,
    GameMapComponent,
    SidebarComponent,
    GameUsersListComponent,
    GameWordsListComponent,
    GameComponent,
    BingoComponent,
    GameWordComponent,
    GameMapModeratorOverlayComponent,
    GameMapPlayerOverlayComponent,
    LoginUserFormComponent,
    GameLogComponent,
    GameChatInputComponent,
    GameLogChatMessageComponent,
    GameLogUserWordMessageComponent,
    GameLogWordRejectedMessageComponent,
    GameLogWordAcceptedMessageComponent
  ],
  imports: [
    BrowserModule,
    HttpClientModule,
    HttpClientJsonpModule,
    AppRoutingModule,
    NgbModule,
    FormsModule,
    SocketIoModule,
    GoogleMapsModule,
    FontAwesomeModule,
    SharedModule
  ],
  providers: [
    {
      provide: APP_INITIALIZER,
      useFactory: (configurationService: ConfigurationService) => {return () => configurationService.loadConfig()},
      deps: [ConfigurationService],
      multi: true
    },
    {
      provide: BASE_PATH,
      useFactory: (configurationService: ConfigurationService) => {return configurationService.getConfig().API_BASE_PATH},
      deps: [ConfigurationService]
    }
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
