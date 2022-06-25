import { ComponentFixture, TestBed } from '@angular/core/testing';

import { GameChatInputComponent } from './game-chat-input.component';

describe('GameChatInputComponent', () => {
  let component: GameChatInputComponent;
  let fixture: ComponentFixture<GameChatInputComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ GameChatInputComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(GameChatInputComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
