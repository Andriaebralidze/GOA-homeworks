// 1)

let currenDate = new Date();
console.log(currentDate);

// 2)

let currentDate = new Date();

console.log("Current Date: " + currentDate);
console.log("Year: " + currentDate.getFullYear());
console.log("Month: " + (currentDate.getMonth() + 1));
console.log("Day: " + currentDate.getDate());
console.log("Day of the week: " + currentDate.getDay());
console.log("Hours: " + currentDate.getHours());
console.log("Minutes: " + currentDate.getMinutes());
console.log("Seconds: " + currentDate.getSeconds());
console.log("Milliseconds: " + currentDate.getMilliseconds());

// 3)

const myp = document.getElementsById("myp");

setInterval(() => {
    const date =  new date();

    myp.textContent = `${date.getHours()}:${date.getMinutes()}:${date.getSeconds}`;
}, 1000)