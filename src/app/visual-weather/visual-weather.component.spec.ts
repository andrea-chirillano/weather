import { ComponentFixture, TestBed } from '@angular/core/testing';

import { VisualWeatherComponent } from './visual-weather.component';

describe('VisualWeatherComponent', () => {
  let component: VisualWeatherComponent;
  let fixture: ComponentFixture<VisualWeatherComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [VisualWeatherComponent]
    });
    fixture = TestBed.createComponent(VisualWeatherComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
