import { Component, EventEmitter, Input, OnInit, Output } from '@angular/core';
import { User } from 'generated/openapi';


@Component({
  selector: 'app-lobby-moderator-form',
  templateUrl: './lobby-moderator-form.component.html',
  styleUrls: ['./lobby-moderator-form.component.scss']
})
export class LobbyModeratorFormComponent implements OnInit {

  constructor() { }

  @Input() users: User[];
  @Output() onFormSubmit: EventEmitter<User> = new EventEmitter();

  public selectedModeratorId: User;

  ngOnInit(): void {

  }

  onSubmit(): void {
    this.onFormSubmit.emit(this.selectedModeratorId);
  }
}
