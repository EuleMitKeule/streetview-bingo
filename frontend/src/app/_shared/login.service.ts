import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class LoginService {

  constructor() { }

  public userToken: string = localStorage.getItem('userToken');

  setUserToken(token: string) {
    localStorage.setItem("userToken", token);
    this.userToken = token;
  }

}
