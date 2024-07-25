const input = require("fs")
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split("\n");

const N = input[0];

input.shift();

let arr = new Array();

input.map((lst) => {
  arr.push(lst.split(" ").map(Number));
});

let result = [];

for (let i = 0; i < N; i++) {
  let cnt = 1;
  for (let j = 0; j < N; j++) {
    if (i !== j) {
      arr[i][0] < arr[j][0] && arr[i][1] < arr[j][1] ? cnt++ : "";
    }
  }
  result.push(cnt);
}

console.log(result.join(" "));
