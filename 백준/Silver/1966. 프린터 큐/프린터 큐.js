const input = require("fs")
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split("\n");

// 테스트케이스 수 T
const T = parseInt(input.shift());

for (let t = 0; t < T; t++) {
  let [N, M] = input.shift().split(" ").map(Number);
  // 정수 list
  let lst = input.shift().split(" ").map(Number);

  let queue = lst.map((value, index) => ({ value, index }));

  // 몇 번째로 인쇄 되는 지 cnt
  let cnt = 0;

  while (true) {
    // 현재 값 shift
    let current = queue.shift();

    if (queue.some((item) => item.value > current.value)) {
      queue.push(current);
    } else {
      cnt++;
      if (current.index === M) {
        console.log(cnt);
        break;
      }
    }
  }
}
