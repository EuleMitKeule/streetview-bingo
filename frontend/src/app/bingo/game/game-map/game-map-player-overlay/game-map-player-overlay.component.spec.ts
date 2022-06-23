import { ComponentFixture, TestBed } from '@angular/core/testing';

import { GameMapPlayerOverlayComponent } from './game-map-player-overlay.component';

describe('GameMapPlayerOverlayComponent', () => {
  let component: GameMapPlayerOverlayComponent;
  let fixture: ComponentFixture<GameMapPlayerOverlayComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ GameMapPlayerOverlayComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(GameMapPlayerOverlayComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
