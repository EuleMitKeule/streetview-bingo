import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { BingoComponent } from './bingo/bingo.component';
import { LoginComponent } from './login/login.component';


const routes: Routes = [
  {path: '', component: LoginComponent},
  {path: 'lobby/:token', component: BingoComponent},
];

@NgModule({
  imports: [RouterModule.forRoot(routes, {useHash: true})],
  exports: [RouterModule]
})
export class AppRoutingModule { }
