const input = require("fs")
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split("\n");

const N = input[0];

input.shift();

const lst = input.map((num) => {
  return num.split(" ");
});

lst.sort((a, b) => a[0] - b[0]);

lst.forEach((element) => {
  console.log(element.join(" "));
});
