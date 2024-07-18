// input 배열에 받아온 값 한 줄씩 저장
const input = require("fs")
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split("\n");

// 마지막 배열 제거
input.pop();

// 한 배열마다 배열로 만들고 숫자로 바꿔서 오름차순 정렬
input.forEach((list) => {
  let lst = list
    .split(" ")
    .map(Number)
    .sort((a, b) => a - b);
  if (lst[0] ** 2 + lst[1] ** 2 === lst[2] ** 2) {
    console.log("right");
  } else {
    console.log("wrong");
  }
});
