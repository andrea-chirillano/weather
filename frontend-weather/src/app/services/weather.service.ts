// En tu servicio, por ejemplo, weather.service.ts

import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root',
})
export class WeatherService {
  private apiUrl = `http://localhost:8000/api/weather`; 
  constructor(private http: HttpClient) {}

  getWeather(countryCode: string, cityInput: string): Observable<any> {
    const params = { countryCode, cityInput };
    return this.http.get<any>(this.apiUrl, { params });
  }
}
