const input = require("fs")
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split("\n")
  .map(Number);

// 숫자 갯수
const N = input.shift();

let stack = [];
let num = 1;
let result = [];
let isPossible = true;
/* 
1,2,3,4 에서 4빼고 
1,2,3 -> 3빼고 
1,2 에서 5 더하고 1,2,5 ...
*/
for (let i = 0; i < N; i++) {
  //   console.log(input[i]);

  const current = input[i];

  while (num <= current) {
    stack.push(num);
    num++;
    result.push("+");
  }

  if (stack[stack.length - 1] === input[i]) {
    stack.pop();
    result.push("-");
  } else {
    isPossible = false;
    break;
  }
}

if (isPossible) {
  console.log(result.join("\n"));
} else {
  console.log("NO");
}
