const input = require("fs")
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split("\n");

// 배열 저장
const lst = input[1].split(" ").map(Number);

// 소수 갯수 저장용 cnt
let cnt = 0;

// for문으로 배열 순회
for (let i = 0; i < input[0]; i++) {
    let zero = 0;
  // 1은 소수가 아니기에 break
  if (lst[i] === 1) {
    continue;
  } else {
    for (let j = 2; j < lst[i]; j++) {
      if (lst[i] % j === 0) {
       zero += 1;
      }
    }
  }
  if (zero === 0) {
    cnt += 1
  }
  
}

console.log(cnt);
