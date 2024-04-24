const fs = require("fs");
const readline = require("readline");

const inputPath = process.platform === "linux" ? "/dev/stdin" : "./test.txt";
const rl = readline.createInterface({
  input: fs.createReadStream(inputPath),
});

let infixExp = "";
const outStack = [];
const operStack = [];

rl.on("line", (line) => {
  infixExp = line;
}).on("close", () => {
  // 1.피연산자의 순서는 바뀌지 않는다. 즉, 피연산자를 만나면 outStack에 push한다.
  // 2.연산자 규칙
  //  1) 자신보다 우선순위가 높은 연산자가 operStack 안에 있으면 해당 연산자를 pop해서 outStack에 push한다.
  //  2) '('는 우선순위와 상관 없이 무조건 push
  //  3) ')'가 나오면 operStack에서 '('를 만날 때까지 pop해서 연산자는 outStack에 push한다.

  for (let i of infixExp) {
    if (["+", "-", "*", "/"].includes(i)) {
      while (true) {
        let top = operStack[operStack.length - 1];
        if (["+", "-"].includes(i) && ["*", "/", "+", "-"].includes(top)) {
          outStack.push(operStack.pop());
        } else if (["*", "/"].includes(i) && ["*", "/"].includes(top)) {
          outStack.push(operStack.pop());
          operStack.push(i);
          break;
        } else {
          operStack.push(i);
          break;
        }
      }
    } else if (i === "(") {
      operStack.push(i);
    } else if (i === ")") {
      while (true) {
        let o = operStack.pop();
        if (o === "(") {
          break;
        } else {
          outStack.push(o);
        }
      }
    } else {
      outStack.push(i);
    }
  }

  while (operStack.length) {
    outStack.push(operStack.pop());
  }
  console.log(outStack.join(""));
});
