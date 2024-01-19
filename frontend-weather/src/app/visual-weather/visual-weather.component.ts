import { Component } from '@angular/core';
import { WeatherService } from '../services/weather.service';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-visual-weather',
  templateUrl: './visual-weather.component.html',
  styleUrls: ['./visual-weather.component.css']
})
export class VisualWeatherComponent {
  iconSunny: string = '../../assets/icons/sunny.svg';
  
  selectedCountry: string = '';
  cityInput: string = '';

  exactTime: string = '';
  weather: string = '';
  temperature: number = 0;
  precipitationProbability: number = 0;
  humidity: number = 0;
  windSpeed: number = 0;

  constructor(private weatherService: WeatherService, private http: HttpClient) {}


  ngOnInit(): void {
    // Llama al servicio para obtener los datos del clima
    this.weatherService.getWeather(this.selectedCountry, this.cityInput).subscribe(data => {
      // Asigna los datos a las propiedades para que puedan ser utilizadas en la plantilla HTML
      this.exactTime = data.exact_time;
      this.weather = data.weather;
      this.temperature = data.temperature_celsius;
      this.precipitationProbability = data.precipitation_probability;
      this.humidity = data.humidity;
      this.windSpeed = data.wind_speed;
    });
  }

  getWeatherInformation() {
    // Obtener los valores del formulario (país y ciudad)
    const countryCode = this.selectedCountry;  // Utiliza la propiedad del componente
    const cityInput = this.cityInput;  // Utiliza la propiedad del componente

    // Realizar la solicitud HTTP al servidor
    this.http.get<any>(`http://localhost:8000/api/weather?countryCode=${countryCode}&cityInput=${cityInput}`)
      .subscribe((data) => {
        // Manejar los datos de respuesta aquí (asignar a las propiedades correspondientes)
        console.log(data);
      });
  }
}
