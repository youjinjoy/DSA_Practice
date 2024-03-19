const fs = require("fs");
const inputPath = process.platform === "linux" ? "/dev/stdin" : "./test.txt";
const stdin = fs
  .readFileSync(inputPath)
  .toString()
  .split("\n")
  .map((str) => str.trim());

const input = (() => {
  let line = 0;
  return () => stdin[line++];
})();

const solution = () => {
  let mySet = new Set();

  for (let i = 0; i < 10; i++) mySet.add(input() % 42);
  console.log(mySet.size);
};

solution();