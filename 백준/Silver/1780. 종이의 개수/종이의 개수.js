const fs = require("fs");
const inputPath = process.platform === "linux" ? "/dev/stdin" : "./test.txt";
const [[N], ...paper] = fs
  .readFileSync(inputPath)
  .toString()
  .trim()
  .split("\n")
  .map((line) => line.split(" ").map(Number));

// 단일 숫자로 채워진 종이인지 확인
// 맞으면 해당 숫자에 대한 개수 +1
// 틀리면 분할해서 재귀
const answer = [0, 0, 0];

function isUniform(n, x, y) {
  const number = paper[x][y];
  for (let i = x; i < x + n; i++) {
    for (let j = y; j < y + n; j++) {
      if (paper[i][j] !== number) {
        return false;
      }
    }
  }
  return true;
}

function recursion(n, x, y) {
  const number = paper[x][y];
  if (isUniform(n, x, y)) {
    addResult(number);
  } else {
    const sn = Number(n / 3);
    for (let i = 0; i < 3; i++) {
      for (let j = 0; j < 3; j++) {
        recursion(sn, x + sn * i, y + sn * j);
      }
    }
  }
}

function addResult(number) {
  if (number === -1) {
    answer[0] += 1;
  } else if (number === 0) {
    answer[1] += 1;
  } else if (number === 1) {
    answer[2] += 1;
  }
}

recursion(N, 0, 0);

for (let item of answer) {
  console.log(item);
}
