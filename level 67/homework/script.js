// 1)
function sumArray(arr) {
    return arr.reduce((acc, num) => acc + num, 0);
}

// 2)
function minMaxArray(arr) {
    let min = Math.min(...arr);
    let max = Math.max(...arr);
    return [min, max];
}

// 3)
function createRandomArray(n) {
    let arr = [];
    for (let i = 0; i < n; i++) {
        arr.push(Math.floor(Math.random() * 100) + 1);
    }
    return arr;
}

// 4)
function squareArray(arr) {
    return arr.map(num => num ** 2);
}

// 5)
function roundNumber(num) {
    return {
        floor: Math.floor(num),
        ceil: Math.ceil(num),
        round: Math.round(num)
    };
}