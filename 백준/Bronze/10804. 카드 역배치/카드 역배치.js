const fs = require("fs");
const inputPath = process.platform === "linux" ? "/dev/stdin" : "./test.txt";
const [...sections] = fs
  .readFileSync(inputPath)
  .toString()
  .trim()
  .split("\n")
  .map((line) => line.split(" ").map(Number));

function reverseCards(start, end) {
  const before = [...cards];
  for (let i = start; i <= end; i++) {
    for (let i = 0; i <= end - start; i++) {
      cards[start + i] = before[end - i];
    }
  }
}

let card = 0;
const cards = Array.from({ length: 21 }, () => card++);

for (let [a, b] of sections) {
  reverseCards(a, b);
}

console.log(cards.slice(1).join(" "));
