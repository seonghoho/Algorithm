const input = require("fs")
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split("\n");

const number = Number(input.shift());
let arr = input.shift().split(" ").map(Number);

const changeNumber = (num) => (num === 1 ? 0 : 1);

input.forEach((el) => {
  const [gender, switchNumber] = el.split(" ").map(Number);

  if (gender === 1) {
    for (let i = switchNumber; i <= number; i += switchNumber) {
      arr[i - 1] = changeNumber(arr[i - 1]);
    }
  } else {
    let num = 0;
    while (
      switchNumber - num - 1 >= 0 &&
      switchNumber + num - 1 < number &&
      arr[switchNumber - num - 1] === arr[switchNumber + num - 1]
    ) {
      arr[switchNumber - num - 1] = changeNumber(arr[switchNumber - num - 1]);
      arr[switchNumber + num - 1] = changeNumber(arr[switchNumber + num - 1]);
      num++;
    }
    arr[switchNumber - 1] = changeNumber(arr[switchNumber - 1]);
  }
});

for (let i = 0; i < arr.length; i += 20) {
  console.log(arr.slice(i, i + 20).join(" "));
}
