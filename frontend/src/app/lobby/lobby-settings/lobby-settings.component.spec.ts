import { ComponentFixture, TestBed } from '@angular/core/testing';

import { LobbySettingsComponent } from './lobby-settings.component';

describe('LobbySettingsComponent', () => {
  let component: LobbySettingsComponent;
  let fixture: ComponentFixture<LobbySettingsComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ LobbySettingsComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(LobbySettingsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
