const fs = require("fs");
const inputPath = process.platform === "linux" ? "/dev/stdin" : "./test.txt";
const S = fs.readFileSync(inputPath).toString().trim();

const partsSet = new Set();

const n = S.length;

for (let window = 1; window <= n; window++) {
  for (let i = 0; i <= n - window; i++) {
    const partS = S.slice(i, i + window);
    partsSet.add(partS);
  }
}

console.log(partsSet.size);
