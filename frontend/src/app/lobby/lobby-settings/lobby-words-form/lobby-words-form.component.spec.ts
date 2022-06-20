import { ComponentFixture, TestBed } from '@angular/core/testing';

import { LobbyWordsFormComponent } from './lobby-words-form.component';

describe('LobbyWordsFormComponent', () => {
  let component: LobbyWordsFormComponent;
  let fixture: ComponentFixture<LobbyWordsFormComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ LobbyWordsFormComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(LobbyWordsFormComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
