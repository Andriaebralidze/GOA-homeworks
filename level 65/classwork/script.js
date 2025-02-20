// 1)

// მსგავსებები:

// ორივე საშუალებას აძლევს მონაცემების შენახვას "კი-ვაც" ფორმატში (key-value pairs).
// ორივე გამოყენებული არის მონაცემების დაჯგუფებისთვის, რათა ხელმისაწვდომი იყოს ერთი ღირებულება გარკვეულ მ ключზე (key).
// ორივეს აქვს დინამიური შემოტანა/წაშლა და შეიძლება შეიცვალოს პროგრამის მიმდინარეობის დროს.
// განმასხვავებები:

// Python Dictionary: პითონში dictionary მოიცავს კლავიშს და შესაბამის ღირებულებებს, ხოლო გასაღებები შეიძლება იყოს ნებისმიერი შეუზღუდავი ტიპის (მაგალითად: სტრიქონი, რიცხვი).
// სინტაქსი: my_dict = {"key": "value", "age": 30}
// Python-ში dictionary-ს ფუნქციები და მეთოდები უფრო ხშირად გამოიყენება ამისთვის, რათა განხორციელდეს მეთოდები, როგორებიცაა .get(), .keys() და ა.შ.

// 2)

let person = {
    name: "John",
    age: 30,
    greet: function() {
        console.log("Hello, " + this.name);
    }
};

person.greet();  // Output: Hello, John

// 3)

function greet(name) {
    console.log("Hello, " + name);
}
greet("Alice");

// 4)

function Person(name, age, occupation) {
    this.name = name;
    this.age = age;
    this.occupation = occupation;
}

let person1 = new Person("Alice", 25, "Engineer");
let person2 = new Person("Bob", 30, "Designer");

console.log(person1.name);  // Output: Alice
console.log(person2.occupation);  // Output: Designer

// 5)

function Car(make, model, year, horsePower, color) {
    this.make = make;
    this.model = model;
    this.year = year;
    this.horsePower = horsePower;
    this.color = color;

    this.increaseHorsePower = function() {
        this.horsePower += 100;
    };
}

let car1 = new Car("Ford", "Mustang", 2020, 450, "Red");
console.log(car1.horsePower);  // Output: 450

car1.increaseHorsePower();
console.log(car1.horsePower);  // Output: 550