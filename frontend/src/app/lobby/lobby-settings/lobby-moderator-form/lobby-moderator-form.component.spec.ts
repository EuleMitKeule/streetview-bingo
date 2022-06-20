import { ComponentFixture, TestBed } from '@angular/core/testing';

import { LobbyInformationFormComponent } from './lobby-moderator-form.component';

describe('LobbyInformationFormComponent', () => {
  let component: LobbyInformationFormComponent;
  let fixture: ComponentFixture<LobbyInformationFormComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ LobbyInformationFormComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(LobbyInformationFormComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
