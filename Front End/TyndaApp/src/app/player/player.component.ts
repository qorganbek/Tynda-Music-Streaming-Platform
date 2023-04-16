import { Component } from '@angular/core';
import { Song } from "../song";

@Component({
  selector: 'app-player',
  templateUrl: './player.component.html',
  styleUrls: ['./player.component.css']
})
export class PlayerComponent  {
  CurrentSong: Song
  NextSong: Song
  PrevSong: Song

  constructor() {
    this.CurrentSong = {} as Song;
    this.NextSong = {} as Song;
    this.PrevSong = {} as Song;
  }


}

