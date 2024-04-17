const fs = require("fs");
const readline = require("readline");

const inputPath = process.platform === "linux" ? "/dev/stdin" : "./test.txt";
const rl = readline.createInterface({
  input: fs.createReadStream(inputPath),
});

let number = [];
rl.on("line", (line) => {
  number.push(line);
}).on("close", () => {
  let l = number.length - 1; // 마지막 0 제외한 길이
  for (let s of number) {
    if (s === "0") break;

    let answer = "yes";
    let l = s.length;
    sl = parseInt(l / 2);

    for (let i = 0; i < sl; i++) {
      if (s[i] !== s[l - 1 - i]) {
        answer = "no";
        break;
      }
    }

    console.log(answer);
  }
});
