const fs = require("fs");
const inputPath = process.platform === "linux" ? "/dev/stdin" : "./test.txt";
const [N] = fs.readFileSync(inputPath).toString().trim().split(" ").map(Number);

if (N % 2 === 0) console.log("CY");
else console.log("SK");
