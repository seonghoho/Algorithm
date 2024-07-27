const input = require("fs")
  .readFileSync("dev/stdin")
  .toString()
  .trim()
  .split("\n");

// 의견 개수
const N = parseInt(input.shift());

// 사용자들이 제출한 난이도 리스트
let lst = input.map(Number).sort((a, b) => a - b);

// 전체의 15%
const jeol = Math.min(Math.round(N * 0.15), Math.floor(N / 2));

// 가운데 값 더한 변수
let sum = 0;
let num = 0;

for (let i = jeol; i < lst.length - jeol; i++) {
  sum += lst[i];
  num++;
}

console.log(N ? Math.round(sum / num) : 0);
