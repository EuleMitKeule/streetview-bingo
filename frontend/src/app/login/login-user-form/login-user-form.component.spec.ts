import { ComponentFixture, TestBed } from '@angular/core/testing';

import { LoginUserFormComponent } from './login-user-form.component';

describe('LoginUserFormComponent', () => {
  let component: LoginUserFormComponent;
  let fixture: ComponentFixture<LoginUserFormComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ LoginUserFormComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(LoginUserFormComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
