const fs = require("fs");
const inputPath = process.platform === "linux" ? "/dev/stdin" : "./test.txt";
const [[N], ...paper] = fs
  .readFileSync(inputPath)
  .toString()
  .trim()
  .split("\n")
  .map((line) => line.split(" ").map(Number));

const answer = [0, 0]; // 하얀색(0), 파란색(1)
function findPaper(n, x, y) {
  const c = paper[x][y];
  for (let i = x; i < x + n; i++) {
    for (let j = y; j < y + n; j++) {
      if (paper[i][j] !== c) {
        const k = Number(n / 2);
        findPaper(k, x, y);
        findPaper(k, x + k, y);
        findPaper(k, x, y + k);
        findPaper(k, x + k, y + k);
        return 0;
      }
    }
  }
  answer[c] += 1;
}

findPaper(N, 0, 0);
console.log(answer.join(" "));
