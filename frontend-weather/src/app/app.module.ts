import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { VisualWeatherComponent } from './visual-weather/visual-weather.component';
import { SunnyComponent } from './sunny/sunny.component';
import { CloudComponent } from './cloud/cloud.component';

@NgModule({
  declarations: [
    AppComponent,
    VisualWeatherComponent,
    SunnyComponent,
    CloudComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
