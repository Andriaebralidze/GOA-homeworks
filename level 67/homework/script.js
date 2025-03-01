// 1)
function sumArray(arr) {
    let sum = 0;
    for (let i = 0; i < arr.length; i++) {
        sum += arr[i];
    }
    return sum;
}

// 2)
function minMaxArray(arr) {
    let min = arr[0];
    let max = arr[0];
    for (let i = 1; i < arr.length; i++) {
        if (arr[i] < min) {
            min = arr[i];
        }
        if (arr[i] > max) {
            max = arr[i];
        }
    }
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
    let squaredArr = [];
    for (let i = 0; i < arr.length; i++) {
        squaredArr.push(arr[i] ** 2);
    }
    return squaredArr;
}

// 5)
function roundNumber(num) {
    let result = {};
    let operations = ['floor', 'ceil', 'round'];
    for (let i = 0; i < operations.length; i++) {
        let operation = operations[i];
        if (operation === 'floor') {
            result.floor = Math.floor(num);
        } else if (operation === 'ceil') {
            result.ceil = Math.ceil(num);
        } else if (operation === 'round') {
            result.round = Math.round(num);
        }
    }
    return result;
}