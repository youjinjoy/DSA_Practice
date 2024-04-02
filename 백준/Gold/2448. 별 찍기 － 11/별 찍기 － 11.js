const fs = require("fs");
const inputPath = process.platform === "linux" ? "/dev/stdin" : "./test.txt";
const N = parseInt(fs.readFileSync(inputPath).toString());
const K = Math.log2(parseInt(N / 3));

function drawTriangle(k) {
  const triangle = [];
  if (k === 0) {
    return ["  *  ", " * * ", "*****"];
  } else {
    const before = drawTriangle(k - 1);
    const base = before[before.length - 1].length;
    const additional = Math.floor(base / 2) + 1;
    const space = " ".repeat(additional);
    for (let i = 0; i < before.length; i++) {
      triangle[i] = space + before[i] + space;
      triangle[i + before.length] = before[i] + " " + before[i];
    }
    return triangle;
  }
}
const result = drawTriangle(K);
console.log(result.join("\n"));
