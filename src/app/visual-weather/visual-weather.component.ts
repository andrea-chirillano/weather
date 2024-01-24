import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { WeatherService } from '../services/weather.service';
import { HttpClient } from '@angular/common/http';
import { Observer } from 'rxjs';

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
    this.weatherService.getWeather(countryCode, cityInput)
      .subscribe({
        next: (data) => {
          const formattedData = this.weatherService.formatWeatherData(data);

          this.selectedCountry = formattedData.countryName || 'Unknown country';
          this.cityInput = formattedData.cityName || 'Unknown city';
          this.exactTime = formattedData.exactTime || 'Unknown time';
          this.weather = formattedData.weather || 'Unknown weather';
          this.temperature = formattedData.temperatureCelsius || 0;
          this.precipitationProbability = formattedData.precipitationProbability || 0;
          this.humidity = formattedData.humidity || 0;
          this.windSpeed = formattedData.windSpeed || 0;

          // Change the status to display information after receiving the response
          this.showWeatherInfo = true;

          // Hide form elements after receiving response
          this.showFormElements = false;

          console.log('Received data:', data);
        }
        ,
        error: (error) => {
          console.error('Error fetching weather data:', error);
        },
        complete: () => {
          // Lógica cuando la operación está completa (equivalente a la función complete anterior)
          console.log('Weather data fetching complete');
        }
    });
  }

}