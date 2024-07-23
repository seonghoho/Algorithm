const { performance } = require("perf_hooks");

// 이진 탐색 함수
function binarySearch(arr, target) {
  let left = 0;
  let right = N - 1;

  while (left <= right) {
    const mid = Math.floor((left + right) / 2);

    if (arr[mid] === target) {
      return true;
    } else if (arr[mid] < target) {
      left = mid + 1;
    } else {
      right = mid - 1;
    }
  }
  return false;
}

const input = require("fs")
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split("\n");

const start = performance.now();

const N = parseInt(input[0]);

let A = input[1]
  .split(" ")
  .map(Number)
  .sort((a, b) => a - b);

const M = parseInt(input[2]);

let B = input[3].split(" ").map(Number);

B.forEach((num) => {
  console.log(binarySearch(A, num) ? 1 : 0);
});

const end = performance.now();
// console.log(end - start);
