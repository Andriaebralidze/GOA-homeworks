// 1)

let score = parseInt(prompt("Enter your score:"));

if (score >= 90 && score <= 100) {
    console.log("Grade A");
} else if (score >= 80 && score < 90) {
    console.log("Grade B");
} else if (score >= 70 && score < 80) {
    console.log("Grade C");
} else if (score >= 60 && score < 70) {
    console.log("Grade D");
} else {
    console.log("Grade F");
}

// 2)

let age = parseInt(prompt("Enter your age:"));

if (age < 13) {
    console.log("You are kid");
} else if (age >= 13 && age < 18) {
    console.log("You are not adult yet");
} else {
    console.log("You are adult");
}

// 3)

let ag = parseInt(prompt("Enter your age:"));

if (ag < 13) {
    console.log("You are kid");
} else if (ag >= 13 && ag < 18) {
    console.log("You are not adult yet");
} else {
    console.log("You are adult");
}

// 4)

let num = 0;
while (num <= 100) {
    console.log(num);
    num++;
}

// 5)

for (let i = 5; i <= 10; i++) {
    console.log(i);
}