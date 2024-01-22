import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { ReactiveFormsModule } from '@angular/forms';
import { HttpClientModule } from '@angular/common/http';
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { VisualWeatherComponent } from './visual-weather/visual-weather.component';
import { SunnyComponent } from './sunny/sunny.component';
import { CloudComponent } from './cloud/cloud.component';
import { RainComponent } from './rain/rain.component';

@NgModule({
  declarations: [
    AppComponent,
    VisualWeatherComponent,
    SunnyComponent,
    CloudComponent,
    RainComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
    ReactiveFormsModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
