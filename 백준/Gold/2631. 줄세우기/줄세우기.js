const fs = require("fs");
const inputPath = process.platform === "linux" ? "/dev/stdin" : "./test.txt";
const [N, ...children] = fs
  .readFileSync(inputPath)
  .toString()
  .split("\n")
  .map(Number);

// LIS: 증가하는 부분 수열 중 길이가 가장 긴 수열 찾기

const arr = Array(N).fill(1); // 처음에 부분 수열의 길이 1로 초기화

for (let i = 1; i < N; i++) {
  for (let j = 0; j < i; j++) {
    if (children[j] < children[i]) {
      arr[i] = Math.max(arr[j] + 1, arr[i]);
    }
  }
}

console.log(N - Math.max(...arr));
