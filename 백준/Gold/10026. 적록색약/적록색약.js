const input = require("fs")
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split("\n");

// N개의 숫자
const N = parseInt(input.shift());

// 2차원 배열로 작성
let lst = input.map((arr) => arr.split(""));

// 방문 체크 배열
let checkArrNormal = Array.from(Array(N), () => Array(N).fill(false));
let checkArrColorBlind = Array.from(Array(N), () => Array(N).fill(false));

let normalCount = 0; // 일반인의 구역 수
let colorBlindCount = 0; // 적록색약의 구역 수

const bfs = (x, y, color, checkArr, isColorBlind) => {
  const queue = [];
  queue.push([x, y]);
  checkArr[x][y] = true;

  const directions = [
    [-1, 0],
    [1, 0],
    [0, -1],
    [0, 1],
  ];

  while (queue.length > 0) {
    let [curX, curY] = queue.shift();

    for (let i = 0; i < 4; i++) {
      let dx = curX + directions[i][0];
      let dy = curY + directions[i][1];

      if (dx >= 0 && dy >= 0 && dx < N && dy < N) {
        // 적록색약일 경우, R과 G 동일
        if (isColorBlind) {
          if (!checkArr[dx][dy] && (color === "R" || color === "G")) {
            if (lst[dx][dy] === "R" || lst[dx][dy] === "G") {
              checkArr[dx][dy] = true;
              queue.push([dx, dy]);
            }
          } else if (!checkArr[dx][dy] && lst[dx][dy] === color) {
            checkArr[dx][dy] = true;
            queue.push([dx, dy]);
          }
        }
        // 일반인의 경우
        else {
          if (!checkArr[dx][dy] && lst[dx][dy] === color) {
            checkArr[dx][dy] = true;
            queue.push([dx, dy]);
          }
        }
      }
    }
  }
};

for (let i = 0; i < N; i++) {
  for (let j = 0; j < N; j++) {
    if (!checkArrNormal[i][j]) {
      normalCount++;
      bfs(i, j, lst[i][j], checkArrNormal, false); // 일반인
    }
    if (!checkArrColorBlind[i][j]) {
      colorBlindCount++;
      bfs(i, j, lst[i][j], checkArrColorBlind, true); // 적록색약
    }
  }
}

console.log(normalCount, colorBlindCount);
