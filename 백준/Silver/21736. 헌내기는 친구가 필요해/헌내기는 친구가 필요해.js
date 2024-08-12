const input = require("fs")
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split("\n");

const [N, M] = input.shift().split(" ").map(Number);

let lst = new Array();

input.map((row) => {
  return lst.push(row.split(""));
});

// 도연이의 위치 파악
let [ix, iy] = [0, 0];

for (let i = 0; i < N; i++) {
  for (let j = 0; j < M; j++) {
    if (lst[i][j] === "I") {
      ix = i;
      iy = j;
      break;
    }
  }
}

const dx = [-1, 1, 0, 0];
const dy = [0, 0, 1, -1];

const dfs = (x, y) => {
  // 범위 밖이거나, X를 만나면 0 return
  if (x < 0 || x >= N || y < 0 || y >= M || lst[x][y] === "X") {
    return 0;
  }

  let cnt = 0;

  if (lst[x][y] === "P") {
    cnt++;
  }
  lst[x][y] = "X";

  for (let i = 0; i < 4; i++) {
    const nx = x + dx[i];
    const ny = y + dy[i];
    cnt += dfs(nx, ny);
  }
  return cnt;
};

const result = dfs(ix, iy);

if (result === 0) {
  console.log("TT");
} else {
  console.log(result);
}
