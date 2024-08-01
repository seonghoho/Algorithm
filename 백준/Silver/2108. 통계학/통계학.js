const input = require("fs")
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split("\n")
  .map(Number);

const N = input.shift();

// 오름차순
let lst = input.sort((a, b) => a - b);

//산술평균
let avg = 0;

lst.forEach((num) => (avg += num));

console.log(Math.round(avg / N) === -0 ? 0 : Math.round(avg / N));

// 중앙값
let half = parseInt(lst.length / 2);
console.log(lst[half]);

// 최빈값
let frequencyMap = new Map();
lst.forEach((num) => {
  frequencyMap.set(num, (frequencyMap.get(num) || 0) + 1);
});

// 최대 빈도수
let maxFrequency = 0;
let many = [];
frequencyMap.forEach((count, num) => {
  if (count > maxFrequency) {
    maxFrequency = count;
    many = [num];
  } else if (count === maxFrequency) {
    many.push(num);
  }
});

many.sort((a, b) => a - b);

let number = many.length > 1 ? many[1] : many[0];
console.log(number);

// 범위
console.log(lst[N - 1] - lst[0]);
