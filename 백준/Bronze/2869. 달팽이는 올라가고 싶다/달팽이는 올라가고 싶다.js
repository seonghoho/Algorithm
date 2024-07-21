const input = require("fs")
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split(" ")
  .map(Number);

const Up = input[0];

const Down = input[1];

const Total = input[2];

const ud = Up - Down;
// 전체에서 1뎁스 뺀 값
const num = Total - Up;

const res = Math.ceil(num / ud) + 1;

console.log(res);
