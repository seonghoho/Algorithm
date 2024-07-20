const input = require("fs")
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split(" ");

const num1 = parseInt(input[0]);
const num2 = parseInt(input[1]);

// 최대공약수 (GCD) 함수
function gcd(a, b) {
  while (b !== 0) {
    let temp = b;
    b = a % b;
    a = temp;
  }
  return a;
}

// 최소공배수 (LCM) 함수
function lcm(a, b) {
  return (a * b) / gcd(a, b);
}

const yak = gcd(num1, num2);
const bae = lcm(num1, num2);

console.log(yak);
console.log(bae);
