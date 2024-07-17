const fs = require("fs");

const input = fs
  .readFileSync("/dev/stdin", "utf-8")
  .toString()
  .trim()
  .split("\n");

// 맨 앞 값을 지워준다.
input.shift();

// array -> Set -> array 과정을 거쳐 중복 제거
let s_arr = [...new Set(input)];

// localeCompare으로 사전순으로 정렬
s_arr = s_arr
  .sort((a, b) => a.length - b.length || a.localeCompare(b))
  .join("\n");

console.log(s_arr);
