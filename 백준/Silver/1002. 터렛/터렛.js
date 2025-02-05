const input = require("fs")
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split("\n");

const T = Number(input[0]);
const results = [];

for (let i = 1; i <= T; i++) {
  const [x1, y1, r1, x2, y2, r2] = input[i].split(" ").map(Number);
  const distanceSquared = (x1 - x2) ** 2 + (y1 - y2) ** 2; // 거리의 제곱
  const rSumSquared = (r1 + r2) ** 2; // 두 반지름 합의 제곱
  const rDiffSquared = (r1 - r2) ** 2; // 두 반지름 차이의 제곱

  if (distanceSquared === 0 && r1 === r2) {
    results.push("-1");
  } else if (
    distanceSquared === rSumSquared ||
    distanceSquared === rDiffSquared
  ) {
    results.push("1");
  } else if (rDiffSquared < distanceSquared && distanceSquared < rSumSquared) {
    results.push("2");
  } else {
    results.push("0");
  }
}

console.log(results.join("\n"));
