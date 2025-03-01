// 1) წამოიღეთ ელემენტები getElementsByClassName'ის საშუალებით

let elements = document.getElementsByClassName("paragraph");
for (let i = 0; i < elements.length; i++) {
  console.log(elements[i]);
}

// 2) წამოიღეთ ელემენტი querySelector'ის მეშვეობით (ჯერ id, შემდეგ class)

let elementById = document.querySelector("#my-paragraph");
console.log(elementById);

let elementByClass = document.querySelector(".paragraph");
console.log(elementByClass);

// 3) წამოიღეთ js'ში img და შეუცვალეთ: src და width

let imgElement = document.querySelector("#my_image");
imgElement.src = "new_image.jpg";
imgElement.width = 500;
console.log(imgElement);

// 4) წამოიღეთ js'ში p და შეუცვალეთ: color, backgroundColor და fontSize

let paragraph = document.querySelector("#my_paragraph");
paragraph.style.color = "blue";
paragraph.style.backgroundColor = "yellow";
paragraph.style.fontSize = "24px";

// 5) js'ის გამოყენებით, შექმენით ახალი p და textNode, შემდეგ textNode ჩასვით პარაგრაფში და პარაგრაფი ჩასვით html'ში მოცემულ div'ში

let newParagraph = document.createElement("p");
let textNode = document.createTextNode("This is a new paragraph!");
newParagraph.appendChild(textNode);

let container = document.querySelector("#container");
container.appendChild(newParagraph);