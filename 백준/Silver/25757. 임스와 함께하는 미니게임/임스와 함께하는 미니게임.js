const fs = require("fs");
const readline = require("readline");

const inputPath = process.platform === "linux" ? "/dev/stdin" : "./test.txt";
const rl = readline.createInterface({
  input: fs.createReadStream(inputPath),
});

let lineCount = 0;
let N = 0;
let limit = 0;

const set = new Set();

rl.on("line", (line) => {
  if (lineCount === 0) {
    [N, limit] = line.split(" ").map((x) => {
      if (!isNaN(Number(x))) return Number(x);
      else if (x === "Y") return 2;
      else if (x === "F") return 3;
      else if (x === "O") return 4;
    });
  } else {
    set.add(line);
  }
  lineCount++;
}).on("close", () => {
  const M = set.size; // 중복 아이디 제외한 인원
  if (M >= limit - 1) {
    // limit에서 본인 제외
    console.log(Math.floor(M / (limit - 1)));
  } else {
    console.log(0);
  }
});
