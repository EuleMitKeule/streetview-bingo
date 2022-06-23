import { ComponentFixture, TestBed } from '@angular/core/testing';

import { GameUsersListComponent } from './game-users-list.component';

describe('GameUsersListComponent', () => {
  let component: GameUsersListComponent;
  let fixture: ComponentFixture<GameUsersListComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ GameUsersListComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(GameUsersListComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
