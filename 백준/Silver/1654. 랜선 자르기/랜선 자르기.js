const input = require("fs")
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split("\n");

const [K, N] = input.shift().split(" ").map(Number);
let lst = input.map(Number);

let start = 1;
let end = Math.max(...lst);
let result = 0;

while (start <= end) {
  let mid = Math.floor((start + end) / 2);
  let count = 0;

  lst.forEach((num) => {
    count += Math.floor(num / mid);
  });

  if (count >= N) {
    result = mid;
    start = mid + 1;
  } else {
    end = mid - 1;
  }
}

console.log(result);
