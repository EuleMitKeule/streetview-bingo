import { Component, Input, OnInit } from '@angular/core';
import { User } from 'generated/openapi';

@Component({
  selector: 'app-user-badge',
  templateUrl: './user-badge.component.html',
  styleUrls: ['./user-badge.component.scss']
})
export class UserBadgeComponent {

  constructor() { }

  @Input() user: User;

}
