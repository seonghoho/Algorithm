const input = require("fs").readFileSync("/dev/stdin").toString().trim();

let num = parseInt(input);
// 해당 횟수에 몇이 최소인지 작성
let memo = new Array(num + 1).fill(0);

for (let i = 2; i < num + 1; i++) {
  memo[i] = memo[i - 1] + 1;
  if (i % 3 === 0) {
    memo[i] = Math.min(memo[i], memo[i / 3] + 1);
  }
  if (i % 2 === 0) {
    memo[i] = Math.min(memo[i], memo[i / 2] + 1);
  }
}

console.log(memo[num]);
