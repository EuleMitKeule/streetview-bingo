import { ComponentFixture, TestBed } from '@angular/core/testing';

import { GameWordsListComponent } from './game-words-list.component';

describe('GameWordsListComponent', () => {
  let component: GameWordsListComponent;
  let fixture: ComponentFixture<GameWordsListComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ GameWordsListComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(GameWordsListComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
