const input = require("fs")
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split("\n");

let when = 0;
let num = 0;

for (let i = 0; i < 3; i++) {
  if (Number(input[i])) {
    when = i;
    num = Number(input[i]);
  }
}

resNum = num + 3 - when;

if (resNum % 3 === 0 && resNum % 5 === 0) {
  console.log("FizzBuzz");
} else if (resNum % 3 === 0 && resNum % 5 !== 0) {
  console.log("Fizz");
} else if (resNum % 3 !== 0 && resNum % 5 === 0) {
  console.log("Buzz");
} else {
  console.log(resNum);
}
