import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import {NotFoundComponent} from "./not-found/not-found.component";
import {SongsComponent} from "./songs/songs.component";

const routes: Routes = [
  {path:  'songs', component: SongsComponent },
  // {path:  '**', component: NotFoundComponent },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
