const fs = require("fs");
const inputPath = process.platform === "linux" ? "/dev/stdin" : "./test.txt";
const [A, B, C] = fs
  .readFileSync(inputPath)
  .toString()
  .trim()
  .split(" ")
  .map(BigInt);
// A를 B번 곱한 수를 C로 나눈 나머지
// A*A*A*A*A*...*A*A = A^B
function pow(a, b) {
  if (b === 1n) return a % C;
  const half = pow(a, b / 2n) % C;
  let result = (half * half) % C;
  if (b % 2n === 0n) {
    return result;
  } else if (b % 2n === 1n) {
    return (result * a) % C;
  }
}

console.log(pow(A, B).toString());
