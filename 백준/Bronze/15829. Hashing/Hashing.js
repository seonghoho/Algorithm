// 31**(자릿수)

const input = require("fs")
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split("\n");

const n = input[0];
const lst = input[1].split("");

let sum = 0;

for (let i = 0; i < n; i++) {
  sum += (lst[i].charCodeAt() - 96) * 31 ** i;
}

console.log(sum);
