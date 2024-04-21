const fs = require("fs");
const readline = require("readline");

const inputPath = process.platform === "linux" ? "/dev/stdin" : "./test.txt";
const rl = readline.createInterface({
  input: fs.createReadStream(inputPath),
});

let lineCount = 0;
const board = [];
let M = 0;
let N = 0;
rl.on("line", (line) => {
  if (lineCount === 0) {
    [N, M] = line.split(" ").map(Number);
  } else {
    board.push(line);
  }
  lineCount++;
}).on("close", () => {
  const black = Array.from({ length: 8 }, (x) => "");
  const white = Array.from({ length: 8 }, (x) => "");

  for (let i = 0; i < 8; i++) {
    for (let j = 0; j < 8; j++) {
      if ((i % 2 === 0 && j % 2 === 0) || (i % 2 === 1 && j % 2 === 1)) {
        black[i] += "B";
        white[i] += "W";
      } else {
        black[i] += "W";
        white[i] += "B";
      }
    }
  }

  let min = 32;

  for (let x = 8; x <= N; x++) {
    for (let y = 8; y <= M; y++) {
      min = Math.min(
        ...[
          min,
          calculateFromBoard(x, y, black),
          calculateFromBoard(x, y, white),
        ]
      );

      // min = Math.min(min, calculateFromBoard(x, y, black));
      // min = Math.min(min, calculateFromBoard(x, y, white));
    }
  }

  console.log(min);
});

function calculateFromBoard(x, y, arr) {
  let result = 0;
  for (let i = x - 8; i < x; i++) {
    for (let j = y - 8; j < y; j++) {
      if (board[i][j] !== arr[i - (x - 8)][j - (y - 8)]) {
        result += 1;
      }
    }
  }
  return result;
}
