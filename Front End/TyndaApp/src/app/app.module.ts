import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { HttpClientModule } from "@angular/common/http";
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { NotFoundComponent } from './not-found/not-found.component';
import { NavbarComponent } from './navbar/navbar.component';
import { SongsComponent } from './songs/songs.component';
import { SongDetailComponent } from './song-detail/song-detail.component';
import {FormsModule} from "@angular/forms";
import { PlayerComponent } from './player/player.component';

@NgModule({
  declarations: [
    AppComponent,
    NotFoundComponent,
    NavbarComponent,
    SongsComponent,
    SongDetailComponent,
    PlayerComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
    FormsModule,
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
