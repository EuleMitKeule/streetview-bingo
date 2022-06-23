import { ComponentFixture, TestBed } from '@angular/core/testing';

import { GameMapComponent } from './game-map.component';

describe('GameMapComponent', () => {
  let component: GameMapComponent;
  let fixture: ComponentFixture<GameMapComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ GameMapComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(GameMapComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
