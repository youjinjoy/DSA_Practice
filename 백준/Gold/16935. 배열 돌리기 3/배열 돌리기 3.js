// 입력
const fs = require("fs");
const inputPath = process.platform === "linux" ? "/dev/stdin" : "./test.txt";
const input = fs.readFileSync(inputPath).toString().trim().split('\n');

const [N, M, R] = input[0].split(' ').map(Number);
let arr = [];
for (let i = 1 ; i <= N ; i++) {
    arr.push(input[i].trim().split(' '));
}
const cal = input[N+1].split(' ');

// 로직
function reverseUpdown() {
    const height = arr.length;
    for (let i = 0 ; i < Math.floor(height/2) ; i++) {
        const temp = arr[i];
        arr[i] = arr[height-i-1];
        arr[height-i-1] = temp;
    }
}

function reverseLeftRight() {
    const height = arr.length;
    for (let i = 0 ; i < height ; i++) {
        arr[i].reverse();
    }
}

function rotateRight() {
    const height = arr.length;
    const width = arr[0].length;
    
    const newArr = Array.from({length: width}, () => Array(height).fill(0));
    for (let i = 0 ; i < height ; i++) {
        for (let j = 0 ; j < width ; j++) {
            newArr[j][height-i-1] = arr[i][j];
        }
    }

    arr = newArr;
}

function rotateLeft() {
    const height = arr.length;
    const width = arr[0].length;
    
    const newArr = Array.from({length: width}, () => Array(height).fill(0));
    for (let i = 0 ; i < height ; i++) {
        for (let j = 0 ; j < width ; j++) {
            newArr[width-j-1][i] = arr[i][j];
        }
    }

    arr = newArr;
}

function moveClockwise() {
    const height = arr.length;
    const width = arr[0].length;

    const hh = Math.floor(height/2);
    const hw = Math.floor(width/2);
    const newArr = Array.from({length: height}, () => Array(width).fill(0));
    
    for (let i = 0 ; i < hh ; i++) {
        for (let j = 0 ; j < hw ; j++) {
            newArr[i][j+hw] = arr[i][j];
            newArr[i][j] = arr[i+hh][j];
            newArr[i+hh][j] = arr[i+hh][j+hw];
            newArr[i+hh][j+hw] = arr[i][j+hw];
        }
    }

    arr = newArr;
}

function moveCounterClockwise() {
    const height = arr.length;
    const width = arr[0].length;

    const hh = Math.floor(height/2);
    const hw = Math.floor(width/2);
    const newArr = Array.from({length: height}, () => Array(width).fill(0));
    for (let i = 0 ; i < hh ; i++) {
        for (let j = 0 ; j < hw ; j++) {
            newArr[i][j] = arr[i][j+hw];
            newArr[i+hh][j] = arr[i][j];
            newArr[i+hh][j+hw] = arr[i+hh][j];
            newArr[i][j+hw] = arr[i+hh][j+hw];
        }
    }

    arr = newArr;
}

for (let c of cal) {
    if (c === '1') {
        reverseUpdown();
    }
    else if (c === '2') {
        reverseLeftRight();
    }
    else if (c === '3') {
        rotateRight();
    }
    else if (c === '4') {
        rotateLeft();
    }
    else if (c === '5') {
        moveClockwise();
    }
    else {
        moveCounterClockwise();
    }

}
const answer = arr.map((row)=>row.join(' ')).join('\n');
console.log(answer);