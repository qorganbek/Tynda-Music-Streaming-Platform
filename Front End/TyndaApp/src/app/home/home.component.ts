import { Component } from '@angular/core';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent {
  data: [number, number, number, number, number, number]

  constructor() {
    this.data = [1,2,3,4,5,6]
  }


}
