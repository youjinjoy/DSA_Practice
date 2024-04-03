const fs = require("fs");
const inputPath = process.platform === "linux" ? "/dev/stdin" : "./test.txt";
const [A, B] = fs
  .readFileSync(inputPath)
  .toString()
  .trim()
  .split(" ")
  .map(Number);

let ans = 0;
function gcd(a, b) {
  if (a % b === 0) {
    ans = b;
    return;
  }
  gcd(b, a % b);
}

if (A > B) {
  gcd(A, B);
} else {
  gcd(B, A);
}

console.log(ans);
console.log(ans * (A / ans) * (B / ans));
