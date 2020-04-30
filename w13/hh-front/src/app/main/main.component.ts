import { Component, OnInit } from '@angular/core';
import {Company} from '../model';
import {CompanyService} from '../companies.service';

@Component({
  selector: 'app-main',
  templateUrl: './main.component.html',
  styleUrls: ['./main.component.css']
})
export class MainComponent implements OnInit {
  
  companies: Company[] = [];

  constructor(public companyService: CompanyService) { }

  ngOnInit(): void {
    this.getCompanies();
  }

  getCompanies(){ 
    this.companyService.getCompanies()
      .subscribe( companies => { this.companies=companies });
  }

}
