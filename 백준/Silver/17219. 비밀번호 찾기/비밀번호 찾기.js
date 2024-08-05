const input = require("fs")
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split("\n");

let lst = new Map();

const [N, M] = input.shift().split(" ");

for (let i = 0; i < N; i++) {
  let [id, pw] = input[i].split(" ");
  lst.set(id, pw);
}

const urls = input.slice(N, N + M);

for (let i = 0; i < M; i++) {
  console.log(lst.get(urls[i]));
}
