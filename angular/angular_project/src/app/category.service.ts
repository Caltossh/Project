import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { Category } from './models';

@Injectable({
  providedIn: 'root'
})
export class CategoryService {
  url = "http://127.0.0.1:8000/api/categories/"
  constructor(private http: HttpClient) { }

  getCategories():Observable<Category[]>{
    return this.http.get<Category[]>(this.url);
  }
}
