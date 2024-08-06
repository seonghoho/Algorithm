const input = require("fs")
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split("\n");

const N = parseInt(input.shift());

const lst = input.map((arr) => arr.split(" ").map(Number));

let white = 0;
let blue = 0;

// 재귀
const isSameColor = (x, y, len) => {
  const color = lst[x][y];
  for (let i = x; i < x + len; i++) {
    for (let j = y; j < y + len; j++) {
      if (lst[i][j] !== color) {
        return false;
      }
    }
  }
  return true;
};

const recursion = (x, y, len) => {
  if (isSameColor(x, y, len)) {
    if (lst[x][y] === 1) {
      blue++;
    } else {
      white++;
    }
  } else {
    const half = len / 2;
    recursion(x, y, half);
    recursion(x, y + half, half);
    recursion(x + half, y, half);
    recursion(x + half, y + half, half);
  }
};

recursion(0, 0, N);

console.log(white);
console.log(blue);
