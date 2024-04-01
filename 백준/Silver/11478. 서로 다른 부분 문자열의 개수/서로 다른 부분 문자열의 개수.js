const fs = require("fs");
const inputPath = process.platform === "linux" ? "/dev/stdin" : "./test.txt";
const S = fs.readFileSync(inputPath).toString().trim();

const hash = {};

const n = S.length;
// 1글자부터 n글자까지 window
let window = 1;
// n글자 크기일 때 멈춤
while (window !== n) {
  for (let i = 0; i <= n - window; i++) {
    const partS = S.slice(i, i + window);
    hash[partS] = (hash[partS] || 0) + 1;
  }
  window += 1;
}
console.log(Object.keys(hash).length + 1); // n글자 케이스 +1 추가
