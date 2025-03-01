// 2) თავიდან გააკეთეთ დროის ამთვლელი მოწყობილობა, რომელიც გამოიტანს მხოლოდ წუთებს და წამებს

function timeCounter() {
    let startTime = Date.now();
    let display = document.getElementById("timeDisplay");
    setInterval(function() {
        let elapsedTime = (Date.now() - startTime) / 1000;
        let minutes = Math.floor(elapsedTime / 60);
        let seconds = Math.floor(elapsedTime % 60);
        display.textContent = `${String(minutes).padStart(2, "0")}:${String(seconds).padStart(2, "0")}`;
    }, 1000);
}

timeCounter();

// 3) setInterval'ის გამოყენებით შექმენით პროგრამა რომელიც დაიწყებს 0'იდან და ყოველ ნახევარ წამში გამოიტანს რიცხვებს (ყველა გამეორებაზე 1'ით გაიზრდება) როდესაც ეს ავა 15'ზე მაშინ გაჩერდეს setInterval

let counter = 0;
let display = document.getElementById("counter");

let interval = setInterval(function() {
    counter++;
    display.textContent = counter;
    if (counter >= 15) {
        clearInterval(interval);
    }
}, 500);

// 4) გამოიტანეთ 3 ბრძანება:
// console.log(1)
// console.log(2)
// console.log(3)

console.log(1);
console.log(2);
console.log(3);