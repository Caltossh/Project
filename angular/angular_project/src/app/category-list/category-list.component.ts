import { Component } from '@angular/core';
import { CategoryService } from '../category.service';

@Component({
  selector: 'app-category-list',
  templateUrl: './category-list.component.html',
  styleUrl: './category-list.component.css'
})
export class CategoryListComponent {
  categories: any

  constructor (private categoryService: CategoryService){}

  ngOnInit():void{
    this.categoryService.getCategories().toPromise().then(
      categories => {this.categories = categories; 
      console.log(this.categories);
  
      },
      
      error=>{console.error(error);}
    );
  }

  showItems(categoryId: number): void {
  console.log('Category ID:', categoryId);
  alert(categoryId);
}

}
