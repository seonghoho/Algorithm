const input = require("fs").readFileSync("/dev/stdin").toString().trim();

let N = Number(input) - 1;

let step = 1;
while (N > 0) {
  N -= step * 6;
  step += 1;
}
console.log(step);
