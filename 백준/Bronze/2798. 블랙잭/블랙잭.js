const input = require("fs")
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split("\n");

const NM = input[0].split(" ");
// 카드 갯수
const N = NM[0];
// 딜러가 부르는 수
const M = NM[1];
// 카드 목록을 오름차순으로
const lst = input[1]
  .split(" ")
  .map(Number)
  .sort((a, b) => a - b);

let max = 0;
let sum = 0;

for (let i = 0; i < lst.length - 2; i++) {
  sum = 0;
  sum += lst[i];
  for (let j = i + 1; j < lst.length - 1; j++) {
    sum = lst[i];
    sum += lst[j];
    for (let k = j + 1; k < lst.length; k++) {
      //   console.log("i = " + i);
      //   console.log("j = " + j);
      //   console.log("k = " + k);
      //   console.log("sum = " + sum);
      //   console.log("lst[k] = " + lst[k]);

      if (sum + lst[k] > max && sum + lst[k] <= M) {
        max = sum + lst[k];
        // console.log("max = " + max);
        // console.log("-------------");
      }
    }
  }
}

console.log(max);
