const input = require("fs")
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split("\n");

const N = Number(input[0]);
const lst_n = input[1].split(" ").map(Number);
const M = Number(input[2]);
const lst_m = input[3].split(" ").map(Number);

let countMap = new Map();

// countMap 함수에 lst_n의 안에 있는 숫자가 있는지 확인하고
// 있으면 그 값에 +1, 없으면 1 추가하는 로직

for (let i = 0; i < N; i++) {
  if (countMap.has(lst_n[i])) {
    countMap.set(lst_n[i], countMap.get(lst_n[i]) + 1);
  } else {
    countMap.set(lst_n[i], 1);
  }
}

let result = [];

for (let j = 0; j < M; j++) {
  if (countMap.has(lst_m[j])) {
    result.push(countMap.get(lst_m[j]));
  } else {
    result.push(0);
  }
}

console.log(result.join(" "));


// const input = require("fs")
//   .readFileSync("example.txt")
//   .toString()
//   .trim()
//   .split("\n");

// const N = Number(input[0]);

// const lst_n = input[1].split(" ").map(Number);

// const M = Number(input[2]);

// const lst_m = input[3].split(" ").map(Number);

// let plus_arr = new Array(10000000).fill(0);
// let minus_arr = new Array(10000000).fill(0);
// let zero = 0;

// for (let i = 0; i < N; i++) {
//   if (lst_n[i] > 0) {
//     plus_arr[lst_n[i]]++;
//   } else if (lst_n[i] < 0) {
//     minus_arr[-lst_n[i]]++;
//   } else {
//     zero++;
//   }
// }

// let result = new Array();

// for (let j = 0; j < M; j++) {
//   if (lst_m[j] > 0) {
//     result.push(plus_arr[lst_m[j]]);
//   } else if (lst_m[j] < 0) {
//     result.push(minus_arr[-lst_m[j]]);
//   } else {
//     result.push(zero);
//   }
// }

// console.log(result.join(" "));
