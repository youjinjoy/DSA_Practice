const fs = require("fs");
const inputPath = process.platform === "linux" ? "/dev/stdin" : "./test.txt";
const input = fs.readFileSync(inputPath).toString().trim();

number = input.split(" ");
a = number[0];
b = number[1];

ra = parseInt(a[2] + a[1] + a[0]);
rb = parseInt(b[2] + b[1] + b[0]);
ra > rb ? console.log(ra) : console.log(rb);