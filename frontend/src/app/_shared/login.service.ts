import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class LoginService {

  constructor() { }

  public userToken: string = localStorage.getItem('userToken');
  public userId: number = Number(localStorage.getItem('userId'));

  setUserToken(token: string) {
    localStorage.setItem("userToken", token);
    this.userToken = token;
  }

  setUserId(id: number) {
    localStorage.setItem("userId", id.toString());
    this.userId = id;
  }

}
