const input = require("fs")
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split("\n");

const N = input.shift();

let lst = input[0]
  .split(" ")
  .map(Number)
  .sort((a, b) => a - b);

let number = N;
let cnt = 0;

for (let num of lst) {
  cnt += number * num;
  number--;
}

console.log(cnt);
