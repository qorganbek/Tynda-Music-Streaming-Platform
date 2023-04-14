import {Component, OnInit} from '@angular/core';
import {Song} from "../song";
import {SongService} from "../song.service";

@Component({
  selector: 'app-songs',
  templateUrl: './songs.component.html',
  styleUrls: ['./songs.component.css']
})
export class SongsComponent  implements OnInit{
  data: Song[];
  loaded: boolean;

  constructor(private service: SongService)  {
    this.data = [];
    this.loaded = true;
  }

  ngOnInit(): void{
    this.getSongs()
  }

  getSongs(): void {
    this.loaded = false;
    this.service.getSongs().subscribe((song) => {
      this.data = song;
      this.loaded = true;
    })
  }

}
