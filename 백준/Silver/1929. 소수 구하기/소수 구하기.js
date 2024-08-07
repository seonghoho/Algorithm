const [M, N] = require("fs")
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split(" ")
  .map(Number);

// N개의 0이 들어간 배열 생성
let lst = Array(N + 1).fill(Number(0));

for (let i = 2; i <= N; i++) {
  if (lst[i] === 0) {
    if (i >= M) console.log(i);

    let num = i;
    while (num <= N) {
      lst[num] = 1;
      num += i;
    }
  }
}
