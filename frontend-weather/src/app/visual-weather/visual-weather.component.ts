import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators  } from '@angular/forms';
import { WeatherService } from '../services/weather.service';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-visual-weather',
  templateUrl: './visual-weather.component.html',
  styleUrls: ['./visual-weather.component.css']
})
export class VisualWeatherComponent {
  showWeatherInfo: boolean = false;
  showFormElements: boolean = true;
  iconSunny: string = '../../assets/icons/sunny.svg';
  
  selectedCountry: string = '';
  cityInput: string = '';

  weatherForm: FormGroup;

  exactTime: string = '';
  weather: string = '';
  temperature: number = 0;
  precipitationProbability: number = 0;
  humidity: number = 0;
  windSpeed: number = 0;

  constructor(private fb: FormBuilder, private weatherService: WeatherService, private http: HttpClient) {
    this.weatherForm = this.fb.group({
      countryCode: ['', Validators.required],
      cityInput: ['', Validators.required]
    });
  }

  getWeatherInformation(event?: Event) {
    if (event) {
      event.preventDefault();
    }
  
    // Get the form values (country and city)
    const countryCode = this.weatherForm.get('countryCode')?.value;
    const cityInput = this.weatherForm.get('cityInput')?.value;
  
    // Print the values to verify
    console.log('Country Code:', countryCode);
    console.log('City Input:', cityInput);
  
    // Verify that the values are not null before making the HTTP request
    if (!countryCode || !cityInput) {
      console.error('Country code or city input is null.');
      return;
    }
  
    // Make the HTTP request to the server
    this.weatherService.getWeather(countryCode, cityInput).subscribe(
      (data) => {
        // Verify that the data received is valid before assigning it
        if (data) {
          this.selectedCountry = data.country_name;
          this.cityInput = data.city_name;
          this.exactTime = data.exact_time;
          this.weather = data.weather;
          this.temperature = data.temperature_celsius;
          this.precipitationProbability = data.precipitation_probability;
          this.humidity = data.humidity;
          this.windSpeed = data.wind_speed;
  
          // Change the status to display information after receiving the response
          this.showWeatherInfo = true;
          
          // Hide form elements after receiving response
          this.showFormElements = false;
        } else {
          console.error('Received invalid data from the server.');
        }
      },
      (error) => {
        console.error('Error fetching weather data:', error);
      }
    );
  }
  
}