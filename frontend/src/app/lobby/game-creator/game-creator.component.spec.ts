import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { GameCreatorComponent } from './game-creator.component';

describe('GameCreatorComponent', () => {
  let component: GameCreatorComponent;
  let fixture: ComponentFixture<GameCreatorComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ GameCreatorComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(GameCreatorComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
