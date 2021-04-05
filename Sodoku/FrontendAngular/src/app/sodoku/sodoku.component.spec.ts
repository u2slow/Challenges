import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { SodokuComponent } from './sodoku.component';

describe('SodokuComponent', () => {
  let component: SodokuComponent;
  let fixture: ComponentFixture<SodokuComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ SodokuComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(SodokuComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
