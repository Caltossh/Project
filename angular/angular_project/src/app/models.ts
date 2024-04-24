export interface Category {
    id: number,
    name: string,
    description: string  
}

export interface Items {
    id: number,
    name: string,
    season: string,
    size: string,
    amount: number,
    price: number,
    description: string,
    category: Category
}

