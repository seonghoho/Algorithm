const input = require("fs")
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split("\n");

// 갯수
const N = input[0];
// 점수 리스트
const lst = input[1].split(" ").map(Number);
// 최댓값
const Max = Math.max(...lst);

let Sum = 0;

lst.forEach((num) => {
  Sum += (num / Max) * 100;
});

console.log((Sum / N).toFixed(2));
