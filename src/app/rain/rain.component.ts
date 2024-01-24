import { Component } from '@angular/core';

@Component({
  selector: 'app-rain',
  templateUrl: './rain.component.html',
  styleUrls: ['./rain.component.css']
})
export class RainComponent {
  raindropIndexes: number[] = Array.from({ length: 100 }, (_, i) => i);
}
