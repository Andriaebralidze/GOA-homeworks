// 1) prompt'ის მეშვეობით შექმენით ორი ცვლადი სადაც მომხმარებელს შემოატანინებთ თითო-თითო რიცხვს და შემდეგ გამოიტანეთ მათი ჯამი

num1 = float(input("input first number: "))
num2 = float(input("input second number: "))

sum = num1 + num2
print("sum:", sum)

// 2) prompt'ის მეშვეობით შექმენით 1 ცვლადი სადაც მომხმარებელი შემოიტანს სახელს და შემდეგ მიესალმეთ

let name = prompt("input your name:");
alert("Hello, " + name + "!");

// 3) შექმენით რაიმე ფორმა, სადაც იქნება name input და submit ღილაკი (არ დაგავიწდეთ რომ name input'ს მისცეთ name attribute), გამოიყენეთ addEventListener იმისთვის რომ submit ღილაკზე დაჭერისას console'ში გამოიტანოს მომხმარებლის შემოტანილი სახელი

const form = document.getElementById('nameForm');
form.addEventListener('submit', function(event) {
    event.preventDefault();
    const name = form.elements['name'].value;
    console.log(name);
});