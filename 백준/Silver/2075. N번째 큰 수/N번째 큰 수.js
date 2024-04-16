const fs = require("fs");
const readline = require("readline");

const inputPath = process.platform === "linux" ? "/dev/stdin" : "./test.txt";
const rl = readline.createInterface({
  input: fs.createReadStream(inputPath),
});

class MinHeap {
  constructor() {
    this.heap = [];
  }

  getParentIndex(i) {
    return Math.floor((i - 1) / 2);
  }
  getLeftChildIndex(i) {
    return 2 * i + 1;
  }
  getRightChildIndex(i) {
    return 2 * i + 2;
  }

  swap(i, j) {
    let tmp = this.heap[i];
    this.heap[i] = this.heap[j];
    this.heap[j] = tmp;
  }

  push(key) {
    this.heap.push(key);

    let index = this.heap.length - 1;
    while (
      index !== 0 &&
      this.heap[this.getParentIndex(index)] > this.heap[index]
    ) {
      this.swap(this.getParentIndex(index), index);
      index = this.getParentIndex(index);
    }

    if (this.heap.length > N) {
      this.pop();
    }
  }

  pop() {
    if (this.heap.length === 0) return null;
    if (this.heap.length === 1) return this.heap.pop();

    const top = this.heap[0];
    this.heap[0] = this.heap.pop();

    let index = 0;
    while (this.getLeftChildIndex(index) < this.heap.length) {
      let smallerChildIndex = this.getLeftChildIndex(index);
      if (
        this.getRightChildIndex(index) < this.heap.length &&
        this.heap[this.getRightChildIndex(index)] < this.heap[smallerChildIndex]
      ) {
        smallerChildIndex = this.getRightChildIndex(index);
      }

      if (this.heap[index] < this.heap[smallerChildIndex]) break;

      this.swap(index, smallerChildIndex);
      index = smallerChildIndex;
    }
    return top;
  }

  peek() {
    console.log(this.heap.length > 0 ? this.heap[0] : null);
  }
}

const pq = new MinHeap();
let lineCount = 0;
let N = 0;

rl.on("line", (line) => {
  if (lineCount === 0) {
    N = parseInt(line);
  } else {
    line
      .split(" ")
      .map(Number)
      .forEach((num) => {
        pq.push(num);
      });
  }
  lineCount++;
}).on("close", () => {
  pq.peek();
});
