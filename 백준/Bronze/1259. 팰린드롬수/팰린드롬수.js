const input = require("fs")
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split("\n");

// 맨 뒤 0 제거
input.pop();

for (let i = 0; i < input.length; i++) {
  let lst = input[i].split("").map(Number);
  let isPelin = true;
  while (lst.length > 1) {
    let first = lst.shift();
    let last = lst.pop();
    if (first != last) {
      isPelin = false;
      break;
    }
  }
  isPelin ? console.log("yes") : console.log("no");
}
