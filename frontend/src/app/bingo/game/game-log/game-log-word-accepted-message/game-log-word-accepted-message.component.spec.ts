import { ComponentFixture, TestBed } from '@angular/core/testing';

import { GameLogWordAcceptedMessageComponent } from './game-log-word-accepted-message.component';

describe('GameLogWordAcceptedMessageComponent', () => {
  let component: GameLogWordAcceptedMessageComponent;
  let fixture: ComponentFixture<GameLogWordAcceptedMessageComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ GameLogWordAcceptedMessageComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(GameLogWordAcceptedMessageComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
