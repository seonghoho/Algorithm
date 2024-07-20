const input = require("fs")
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split("\n")
  .map(Number);

input.shift();

while (input.length > 0) {
  let floor = input.shift();
  let room = input.shift();

  // 2차원 배열 생성
  let apt = Array.from(Array(floor + 1), () => Array(room + 1).fill(0));

  // 0층 초기화
  for (let n = 1; n <= room; n++) {
    apt[0][n] = n;
  }

  for (let i = 1; i <= floor; i++) {
    for (let j = 1; j <= room; j++) {
      apt[i][j] = apt[i][j - 1] + apt[i - 1][j];
    }
  }
  console.log(apt[floor][room]);
}
