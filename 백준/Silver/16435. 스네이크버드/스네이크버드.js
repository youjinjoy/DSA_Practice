const fs = require("fs");
const inputPath = process.platform === "linux" ? "/dev/stdin" : "./test.txt";
const [[N, L], heights] = fs
  .readFileSync(inputPath)
  .toString()
  .trim()
  .split("\n")
  .map((line) => line.split(" ").map(Number));

let snakeBird = L;
heights.sort((a, b) => a - b);
for (let h of heights) {
  if (h <= snakeBird) {
    snakeBird += 1;
  }
}

console.log(snakeBird);
