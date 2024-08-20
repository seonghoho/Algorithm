const input = require("fs")
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split(" ");

const [N, K] = input.map(Number);

// 숫자 적힌 배열
let arr = new Array(N + 1).fill(0);
for (let i = 1; i <= N; i++) {
  arr[i] = i;
}
arr.shift();

// 결과 담을 배열
let result = [];
let index = 0;

while (arr.length > 0) {
  index = (index + K - 1) % arr.length;
  result.push(arr.splice(index, 1));
}

console.log(`<${result.join(", ")}>`);
