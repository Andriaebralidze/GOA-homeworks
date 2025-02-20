// 2)

// Object Constructor არის სპეციალური ფუნქცია, რომელიც გამოიყენება ობიექტების შესაქმნელად. როდესაც ფუნქცია მიმდინარეობს new ოპერატორის გამოყენებით, ის ქმნის ახალ ობიექტს, რომელსაც აქვს ყველა ის property და მეთოდი, რაც ფუნქციაშია განსაზღვრული. this key-სი აღნიშნავს ახალ ობიექტს, რომელსაც ასახავს კონსტრუქტორი.

// 4)

function Book(title, author, year, genre, pages) {
    this.title = title;
    this.author = author;
    this.year = year;
    this.genre = genre;
    this.pages = pages;
}

let book1 = new Book("1984", "George Orwell", 1949, "Dystopian", 328);
let book2 = new Book("To Kill a Mockingbird", "Harper Lee", 1960, "Fiction", 281);

console.log(book1.title);
console.log(book2.pages);

// 5)

function Motorcycle(make, model, year, engineCapacity) {
    this.make = make;
    this.model = model;
    this.year = year;
    this.engineCapacity = engineCapacity;

    this.startEngine = function() {
        console.log(this.make + " " + this.model + " engine started!");
    };
}

let motorcycle1 = new Motorcycle("Harley-Davidson", "Street 750", 2020, 750);
let motorcycle2 = new Motorcycle("Yamaha", "YZF-R1", 2021, 998);

console.log(motorcycle1.model);
motorcycle1.startEngine();