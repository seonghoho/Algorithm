const input = require("fs").readFileSync("/dev/stdin").toString().split(" ");
const num = parseInt(input[0]);
const len = parseInt(input[1]);
let up = BigInt(1);
let down = BigInt(1);

for (let i = 0; i < len; i++) {
  up *= BigInt(num) - BigInt(i);
  down *= BigInt(i + 1);
}
let res = (up / down + "").split("n");

num - len ? console.log(res[0]) : console.log(1);
