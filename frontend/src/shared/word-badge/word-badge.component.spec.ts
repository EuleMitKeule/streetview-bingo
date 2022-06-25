import { ComponentFixture, TestBed } from '@angular/core/testing';

import { WordBadgeComponent } from './word-badge.component';

describe('WordBadgeComponent', () => {
  let component: WordBadgeComponent;
  let fixture: ComponentFixture<WordBadgeComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ WordBadgeComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(WordBadgeComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
