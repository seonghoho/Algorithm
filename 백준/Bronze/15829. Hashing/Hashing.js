// 31**(자릿수)

const input = require("fs")
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split("\n");

const n = input[0];
const lst = input[1].split("");

const r = 31n;
const M = 1234567891n;

let sum = 0n;
let pow = 1n;

for (let i = 0; i < n; i++) {
  sum += BigInt(lst[i].charCodeAt() - 96) * pow;
  pow *= r;
}

if (sum >= M) sum %= M;

console.log(Number(sum));