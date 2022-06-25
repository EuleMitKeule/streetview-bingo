import { ComponentFixture, TestBed } from '@angular/core/testing';

import { GameLogChatMessageComponent } from './game-log-chat-message.component';

describe('GameLogChatMessageComponent', () => {
  let component: GameLogChatMessageComponent;
  let fixture: ComponentFixture<GameLogChatMessageComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ GameLogChatMessageComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(GameLogChatMessageComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
