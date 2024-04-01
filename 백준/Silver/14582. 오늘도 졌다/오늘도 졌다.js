const fs = require("fs");
const inputPath = process.platform === "linux" ? "/dev/stdin" : "./test.txt";
const [J, G] = fs
  .readFileSync(inputPath)
  .toString()
  .trim()
  .split("\n")
  .map((line) => line.split(" ").map(Number));

let answer = "No";
let scoreJ = 0;
let scoreG = 0;
for (let i = 0; i < 9; i++) {
  scoreJ += J[i];
  if (scoreJ > scoreG) {
    answer = "Yes";
    break;
  }
  scoreG += G[i];
}

console.log(answer);
