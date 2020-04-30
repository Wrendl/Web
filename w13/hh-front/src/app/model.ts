export class Company {
    id: number;
    name: string;
    description: string;
    city: string;
    address: string;
  }

export class Vacancy {
    id: number;
    name: string;
    salary: number;
  }
  
  export class LoginResponse {
    token: string;
  }