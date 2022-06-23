import { ComponentFixture, TestBed } from '@angular/core/testing';

import { LobbyInformationComponent } from './lobby-information.component';

describe('LobbyInformationComponent', () => {
  let component: LobbyInformationComponent;
  let fixture: ComponentFixture<LobbyInformationComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ LobbyInformationComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(LobbyInformationComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
