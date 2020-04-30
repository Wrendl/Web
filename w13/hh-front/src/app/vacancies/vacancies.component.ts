import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import {CompanyService} from "../companies.service";
import {Company, Vacancy} from "../model";

@Component({
  selector: 'app-vacancies',
  templateUrl: './vacancies.component.html',
  styleUrls: ['./vacancies.component.css']
})
export class VacanciesComponent implements OnInit {
  vacancies: Vacancy[] = []

  constructor(private route: ActivatedRoute, private companyService: CompanyService) { }

  ngOnInit(): void {
    this.getVacancies();
  }

  getVacancies(){
    const id = +this.route.snapshot.paramMap.get('id');

    this.companyService.getVacancies(id).subscribe(vacancies => this.vacancies = vacancies);
  }

}
