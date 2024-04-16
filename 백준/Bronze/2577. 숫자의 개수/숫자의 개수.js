const fs = require("fs");
const inputPath = process.platform === "linux" ? "/dev/stdin" : "./test.txt";
const [A, B, C] = fs
  .readFileSync(inputPath)
  .toString()
  .trim()
  .split("\n")
  .map(Number);

let result = A * B * C;
result = result.toString();
const answer = Array(10).fill(0);

for (let num of result) {
  answer[Number(num)] += 1;
}

console.log(answer.join("\n"));
