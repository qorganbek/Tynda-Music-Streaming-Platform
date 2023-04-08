import { Injectable } from '@angular/core';
import {HttpClient} from "@angular/common/http";
import {Observable} from "rxjs";
import {Song} from "./song";

@Injectable({
  providedIn: 'root'
})
export class SongService {
  url = 'http://localhost:8000/api/songs/';
  constructor(private client: HttpClient) { }

  getSongs(): Observable<Song[]> {
    return this.client.get<Song[]>(this.url)
  }

}
