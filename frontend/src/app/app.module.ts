import { BrowserModule } from '@angular/platform-browser';
import { APP_INITIALIZER, NgModule } from '@angular/core';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { HttpClientJsonpModule, HttpClientModule } from '@angular/common/http';
import { NgbModule } from '@ng-bootstrap/ng-bootstrap';
import { LoginComponent } from './login/login.component';
import { LobbyComponent } from './lobby/lobby.component';
import { FormsModule } from '@angular/forms';
import { BASE_PATH } from 'generated/openapi';
import { ConfigurationService } from './_shared/configuration.service';
import { SocketIoModule } from 'ngx-socket-io';
import { LobbyUsersListComponent } from './lobby/lobby-users-list/lobby-users-list.component';
import { LobbyInformationComponent } from './lobby/lobby-information/lobby-information.component';
import { LobbyModeratorFormComponent } from './lobby/lobby-settings/lobby-moderator-form/lobby-moderator-form.component';
import { MenuCardComponent } from './menu-card/menu-card.component';
import { LobbySettingsComponent } from './lobby/lobby-settings/lobby-settings.component';
import { LobbyWordsFormComponent } from './lobby/lobby-settings/lobby-words-form/lobby-words-form.component';
import { GoogleMapsModule } from '@angular/google-maps';
import { GameMapComponent } from './lobby/game/game-map/game-map.component';


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
    GameMapComponent
  ],
  imports: [
    BrowserModule,
    HttpClientModule,
    HttpClientJsonpModule,
    AppRoutingModule,
    NgbModule,
    FormsModule,
    SocketIoModule,
    GoogleMapsModule
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
