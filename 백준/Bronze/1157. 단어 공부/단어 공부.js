const fs = require("fs");
const inputPath = process.platform === "linux" ? "/dev/stdin" : "./test.txt";
let word = fs.readFileSync(inputPath).toString().trim();

word = word.toUpperCase();
// 다른 사람 풀이 참고 아이디어
// count 배열: 알파벳 숫자 만큼 0으로 채워진 배열

const count = Array(26).fill(0); // A~Z : "Z".charCodeAt() - "A".charCodeAt() + 1 = 90 - 65 + 1
for (let w of word) {
  count[w.charCodeAt() - 65] += 1;
}

let isDup = false;
let max = Math.max(...count);
let index = count.indexOf(max);

for (let i = 0; i < count.length; i++) {
  if (index !== i && count[i] === max) {
    isDup = true;
    break;
  }
}
console.log(isDup ? "?" : String.fromCharCode(index + 65));
