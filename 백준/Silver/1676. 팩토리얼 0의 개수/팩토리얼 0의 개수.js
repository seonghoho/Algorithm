const input = require("fs").readFileSync("/dev/stdin").toString().trim();

const N = parseInt(input);

let cnt = 0;

for (let i = 5; i <= N; i *= 5) {
  cnt += Math.floor(N / i);
}

console.log(cnt);
