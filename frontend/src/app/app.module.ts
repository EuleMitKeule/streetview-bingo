import { BrowserModule } from '@angular/platform-browser';
import { APP_INITIALIZER, NgModule } from '@angular/core';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { HttpClientModule } from '@angular/common/http';
import { NgbModule } from '@ng-bootstrap/ng-bootstrap';
import { LoginComponent } from './login/login.component';
import { LobbyComponent } from './lobby/lobby.component';
import { FormsModule } from '@angular/forms';
import { GameCreatorComponent } from './lobby/game-creator/game-creator.component';
import { GameComponent } from './lobby/game/game.component';
import { BASE_PATH } from 'generated/openapi';
import { ConfigurationService } from './_shared/configuration.service';
import { SocketIoModule } from 'ngx-socket-io';


@NgModule({
  declarations: [
    AppComponent,
    LoginComponent,
    LobbyComponent,
    GameCreatorComponent,
    GameComponent
  ],
  imports: [
    BrowserModule,
    HttpClientModule,
    AppRoutingModule,
    NgbModule,
    FormsModule,
    SocketIoModule
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
