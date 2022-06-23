import { Component, EventEmitter, Input, OnInit, Output } from '@angular/core';
import { User, UsersService } from 'generated/openapi';
import { LoginService } from 'src/app/_shared/login.service';

@Component({
  selector: 'app-login-user-form',
  templateUrl: './login-user-form.component.html',
  styleUrls: ['./login-user-form.component.scss']
})
export class LoginUserFormComponent implements OnInit{

  constructor(
    private loginService: LoginService,
    private usersService: UsersService) { }

  @Input() submitText: string = "Submit";

  @Output() loginUserFormSubmit: EventEmitter<User> = new EventEmitter<User>();

  public name: string;
  public color: string;

  private currentUser: User;

  ngOnInit(): void {
    this.currentUser = this.loginService.user;
    
    if (this.currentUser) {
      this.name = this.currentUser.name;
      this.color = this.currentUser.color;
    }
    else {
      this.usersService.createUser({
        name: this.name,
        color: this.color
      }).subscribe(user => {
        this.currentUser = user;
      });
    }
  }

  onSubmit(): void {
    this.usersService.updateUser(this.currentUser.id, {
      name: this.name,
      color: this.color
    }).subscribe(user => {
      this.loginService.setUser(user);
      this.currentUser = user;
      this.loginUserFormSubmit.emit(this.currentUser);
    });
  }
}
