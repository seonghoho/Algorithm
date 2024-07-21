const input = require("fs").readFileSync("/dev/stdin").toString().trim();

const N = parseInt(input);

let cnt = 0;
let num = 666;

while (cnt < N) {
  if (num.toString().includes("666")) {
    cnt++;
  }
  if (cnt < N) {
    num++;
  }
}

console.log(num);
