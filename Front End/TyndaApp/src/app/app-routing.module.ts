import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import {NotFoundComponent} from "./not-found/not-found.component";
import {MainComponent} from "./main/main.component";
import {SongsComponent} from "./songs/songs.component";

const routes: Routes = [
  {path:  '', component: MainComponent },
  {path:  'songs', component: SongsComponent },
  {path:  '**', component: NotFoundComponent },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
