const input = require("fs")
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split("\n");

const N = input.shift();

let lst = input.map((p) => {
  return p.split(" ").map(Number);
});

lst.sort((a, b) => {
  if (a[1] === b[1]) {
    return a[0] - b[0];
  } else {
    return a[1] - b[1];
  }
});

let result = lst.map((point) => point.join(" ")).join("\n");

console.log(result);

