import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { GameComponent } from './lobby/game/game.component';
import { LobbyComponent } from './lobby/lobby.component';
import { LoginComponent } from './login/login.component';


const routes: Routes = [
  {path: '', component: LoginComponent},
  {path: 'lobby/:token', component: LobbyComponent},
  {path: 'lobby/:lobbyToken/game/:gameToken', component: GameComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes, {useHash: true})],
  exports: [RouterModule]
})
export class AppRoutingModule { }
