const { resolve } = require("dns/promises");

// 숫자 입력받기
const input = require("fs").readFileSync("/dev/stdin").toString().trim();

let res = 0;

// 1에서 입력 받은 숫자까지 for문 순회
for (let i = 1; i < input; i++) {
  let sum = 0;
  // 해당 값 i와 i의 각 자릿수의 수를 더하는 과정
  sum += i;
  //   console.log("i = " + i);
  let arr = (i + "").split("").map(Number);

  arr.forEach((num) => {
    sum += num;
    // console.log("num = " + num);
  });
  //   console.log("sum = " + sum);
  //   console.log("---------");

  if (sum === Number(input)) {
    res += i;
    break;
  }
}

if (res) {
  console.log(res);
} else {
  console.log(0);
}
