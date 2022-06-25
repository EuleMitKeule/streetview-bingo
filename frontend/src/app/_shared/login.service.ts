import { Injectable } from '@angular/core';
import { Lobby, User } from 'generated/openapi';

@Injectable({
  providedIn: 'root'
})
export class LoginService {

  constructor() { }

  get user(): User {
    return JSON.parse(localStorage.getItem("user"));
  }

  setUser(user: User) {
    localStorage.setItem("user", JSON.stringify(user));
  }
}
