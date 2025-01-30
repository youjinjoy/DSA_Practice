const fs = require('fs');

const filePath = process.platform === 'linux' ? '/dev/stdin' : 'test.txt';
let input = fs.readFileSync(filePath).toString().trim().split('\n');

const [N, M, R] = input[0].split(' ').map(Number);
const arr = [];
for (let i = 1; i <= N; i++) {
  arr.push(input[i].split(' '));
}

const end = (N < M ? Math.floor(N / 2) : Math.floor(M / 2)) - 1;
for (let count = 0; count < R; count++) {
  for (let i = 0; i <= end; i++) {
    const temp = arr[i][i];

    const n = N - i;
    const m = M - i;

    for (let y = i; y < m - 1; y++) {
      arr[i][y] = arr[i][y + 1];
    }
    for (let x = i; x < n - 1; x++) {
      arr[x][m - 1] = arr[x + 1][m - 1];
    }
    for (let y = m - 2; y >= i; y--) {
      arr[n - 1][y + 1] = arr[n - 1][y];
    }
    for (let x = n - 2; x >= i; x--) {
      arr[x + 1][i] = arr[x][i];
    }

    arr[i + 1][i] = temp;
  }
}

console.log(arr.map((row) => row.join(' ')).join('\n'));
