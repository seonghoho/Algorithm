// const input = require("fs")
//   .readFileSync("example.txt")
//   .toString()
//   .trim()
//   .split("\n");

// // 배열 저장
// const lst = input[1].split(" ").map(Number);

// // 소수 갯수 저장용 cnt
// let cnt = 0;

// // for문으로 배열 순회
// for (let i = 0; i < input[0]; i++) {
//     let zero = 0;
//   // 1은 소수가 아니기에 break
//   if (lst[i] === 1) {
//     continue;
//   } else {
//     for (let j = 2; j < lst[i]; j++) {
//       if (lst[i] % j === 0) {
//        zero += 1;
//       }
//     }
//   }
//   if (zero === 0) {
//     cnt += 1
//   }

// }

// console.log(cnt);

// 에라토테네스의 체
const input = require("fs")
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split("\n");

const n = parseInt(input[0]);
const lst = input[1].split(" ").map(Number);

const maxValue = Math.max(...lst);

const isPrime = new Array(maxValue + 1).fill(true);
isPrime[0] = isPrime[1] = false;

for (let i = 2; i * i <= maxValue; i++) {
  if (isPrime[i]) {
    for (let j = i * i; j <= maxValue; j += i) {
      isPrime[j] = false;
    }
  }
}

let cnt = 0;
for (let i = 0; i < n; i++) {
  if (isPrime[lst[i]]) {
    cnt += 1;
  }
}

console.log(cnt);
