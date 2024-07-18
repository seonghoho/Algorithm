// 각 줄에 해당하는 값 저장
const input = require("fs")
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split("\n");

// 총 갯수
const total = input[0];

// 사이즈별 갯수 배열
const lst = input[1].split(" ");

// 티셔츠, 펜 묶음 수
const tp = input[2].split(" ");

// 티셔츠 묶음 수
const t = tp[0];

// 펜 묶음 수
const p = tp[1];

// 출력값은 0 => t씩 몇 묶음 주문해야하는가
// 1 => p자루씩 몇 묶음, 나머지 몇개

let count = 0;

lst.forEach((num) => {
  count += Math.ceil(num / t);
});

console.log(count);

console.log(Math.floor(total / p) + " " + (total % p));
