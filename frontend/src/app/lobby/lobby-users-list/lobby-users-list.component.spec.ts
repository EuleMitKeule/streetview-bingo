import { ComponentFixture, TestBed } from '@angular/core/testing';

import { LobbyUsersListComponent } from './lobby-users-list.component';

describe('LobbyUsersListComponent', () => {
  let component: LobbyUsersListComponent;
  let fixture: ComponentFixture<LobbyUsersListComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ LobbyUsersListComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(LobbyUsersListComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
