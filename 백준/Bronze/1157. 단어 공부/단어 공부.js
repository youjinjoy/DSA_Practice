const fs = require("fs");
const inputPath = process.platform === "linux" ? "/dev/stdin" : "./test.txt";
let word = fs.readFileSync(inputPath).toString().trim();

// 소문자의 경우 대문자로 만든다.
word = word.toUpperCase();

// 아이디어 1
// word에 있는 알파벳들을 딕셔너리로 만든다.
// word 내 알파벳을 순회하면서 해당하는 알파벳에 +1을 한다.

// 아이디어 2 (v)
// word 내 알파벳을 순회하면서 이미 딕셔너리에 있던 key면 value에 +1, 없던 key면 새로 만들어 1로 초기화한다.
const dict = {};
for (let alphabet of word) {
  dict[alphabet] = dict[alphabet] + 1 || 1;
}

// 딕셔너리를 순회하면서 더 큰 값이 있으면 그 값을 정답으로.
// 순회할 때 max 값을 저장한다.
// 같은 값이면 '?'
let answer = "";
let max = 0;
for (const [key, value] of Object.entries(dict)) {
  if (value > max) {
    max = value;
    answer = key;
  } else if (value === max && key !== answer) {
    answer = "?";
  }
}

console.log(answer);
