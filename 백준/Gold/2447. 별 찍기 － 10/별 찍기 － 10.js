const fs = require("fs");
const inputPath = process.platform === "linux" ? "/dev/stdin" : "./test.txt";
const [[N]] = fs
  .readFileSync(inputPath)
  .toString()
  .trim()
  .split("\n")
  .map((line) => line.split(" ").map(Number));

// N은 3의 거듭제곱

function drawAll(n) {
  if (n === 1) {
    return ["*"];
  } else {
    const sn = Number(n / 3);
    const stars = drawAll(sn);
    // console.log("stars", stars);
    let temp = [];
    for (let i = 0; i < n; i++) {
      if (i < sn) {
        temp[i] = stars[i % sn].repeat(3);
      } else if (i < sn * 2) {
        temp[i] = stars[i % sn] + " ".repeat(sn) + stars[i % sn];
      } else if (i < sn * 3) {
        temp[i] = stars[i % sn].repeat(3);
      }
    }
    return temp;
  }
}

stars = drawAll(N);
console.log(stars.join("\n"));
