const fs = require("fs");
const inputPath = process.platform === "linux" ? "/dev/stdin" : "./test.txt";
const [[nA, nB], [...A], [...B]] = fs
  .readFileSync(inputPath)
  .toString()
  .trim()
  .split("\n")
  .map((line) => line.split(" ").map(Number));

const setA = new Set(A);
const setB = new Set(B);

const intersection = setA.forEach((a) => {
  if (setB.has(a)) setA.delete(a);
});

const answer = [...setA].sort((a, b) => a - b);
console.log(answer.length);
console.log(answer.join(" "));
