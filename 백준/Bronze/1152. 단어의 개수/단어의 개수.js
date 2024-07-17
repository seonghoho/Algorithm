const input = require("fs").readFileSync("/dev/stdin").toString();

let newArr = input.trim().split(" ");

let cnt = 0;

for (let i = 0; i < newArr.length; i++) {
  if (newArr[i] !== "") {
    cnt++;
  }
}

console.log(cnt);
