import { ComponentFixture, TestBed } from '@angular/core/testing';

import { GameLogWordRejectedMessageComponent } from './game-log-word-rejected-message.component';

describe('GameLogWordRejectedMessageComponent', () => {
  let component: GameLogWordRejectedMessageComponent;
  let fixture: ComponentFixture<GameLogWordRejectedMessageComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ GameLogWordRejectedMessageComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(GameLogWordRejectedMessageComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
