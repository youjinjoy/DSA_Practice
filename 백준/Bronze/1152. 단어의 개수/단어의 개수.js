const fs = require("fs");
const inputPath = process.platform === "linux" ? "/dev/stdin" : "./test.txt";
const s = fs.readFileSync(inputPath).toString().trim().split(" ");

if (s[0] === "") {
  console.log(0);
} else {
  console.log(s.length);
}
