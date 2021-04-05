import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { Sodoku2Component } from './sodoku2.component';

describe('Sodoku2Component', () => {
  let component: Sodoku2Component;
  let fixture: ComponentFixture<Sodoku2Component>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ Sodoku2Component ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(Sodoku2Component);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
