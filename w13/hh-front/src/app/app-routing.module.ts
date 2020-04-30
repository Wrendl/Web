import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { MainComponent } from './main/main.component';
import { VacanciesComponent } from './vacancies/vacancies.component';

const routes: Routes = [
  { path: '', component: MainComponent},
  { path: 'company/:id', component: VacanciesComponent}

];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
