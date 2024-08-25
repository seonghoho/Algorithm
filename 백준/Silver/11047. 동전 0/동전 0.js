const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

const [N, K] = input.shift().split(" ").map(Number);
const lst = input.map(Number);
let money = K;
let coin = 0;

for (let i = lst.length - 1; i >= 0; i--) {
  if (money >= lst[i]) {
    coin += Math.floor(money / lst[i]);
    money = money % lst[i];
  }
  if (money === 0) {
    break;
  }
}

console.log(coin);
