import { Injectable } from '@angular/core';
import { Lobby, User } from 'generated/openapi';

@Injectable({
  providedIn: 'root'
})
export class LoginService {

  constructor() { }

  public user: User = JSON.parse(localStorage.getItem("user"));

  setUser(user: User) {
    localStorage.setItem("user", JSON.stringify(user));
    this.user = user;
  }
}
