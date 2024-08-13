const input = require("fs")
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split("\n");

const [N, M] = input.shift().split(" ");

let lst = input[0]
  .split(" ")
  .map(Number)
  .sort((a, b) => a - b);

let sum = 0;
let max = 0;

for (let i = 0; i < lst.length - 2; i++) {
  sum = 0;
  sum += lst[i];
  for (let j = i + 1; j < lst.length - 1; j++) {
    sum = lst[i];
    sum += lst[j];
    for (let k = j + 1; k < lst.length; k++) {
      if (max < sum + lst[k] && sum + lst[k] <= M) max = sum + lst[k];
    }
  }
}

console.log(max);
