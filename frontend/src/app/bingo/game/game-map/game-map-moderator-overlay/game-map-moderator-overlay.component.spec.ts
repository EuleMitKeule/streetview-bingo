import { ComponentFixture, TestBed } from '@angular/core/testing';

import { GameMapModeratorOverlayComponent } from './game-map-moderator-overlay.component';

describe('GameMapModeratorOverlayComponent', () => {
  let component: GameMapModeratorOverlayComponent;
  let fixture: ComponentFixture<GameMapModeratorOverlayComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ GameMapModeratorOverlayComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(GameMapModeratorOverlayComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
