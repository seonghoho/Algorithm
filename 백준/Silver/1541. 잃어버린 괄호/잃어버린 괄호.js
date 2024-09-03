const input = require("fs").readFileSync("/dev/stdin").toString().trim();

let sep = input.split("-");

let sums = sep.map((elem) => {
  let sum = 0;
  let numbers = elem.split("+");
  for (let num of numbers) {
    sum += parseInt(num);
  }
  return sum;
});

let result = sums[0];
for (let i = 1; i < sums.length; i++) {
  result -= sums[i];
}

console.log(result);
