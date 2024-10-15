const input = require("fs")
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split("\n");

let res = input.slice(1);

const len = res.unshift();

let where = 0;
let arr = "";

while (res[0] !== "KBS1") {
  let idx1 = res.indexOf("KBS1");
  if (idx1 > where) {
    if (res[where + 1] === "KBS1") {
      let curEl = res[where];
      res[where] = res[where + 1];
      res[where + 1] = curEl;
      arr += 3;
      where += 1;
    } else {
      arr += 1;
      where += 1;
    }
  } else if (idx1 <= where) {
    if (res[where - 1] === "KBS1") {
      where -= 1;
      arr += 2;
    } else {
      let curEl = res[where];
      res[where] = res[where - 1];
      res[where - 1] = curEl;
      arr += 4;
      where -= 1;
    }
  }
}

while (res[1] !== "KBS2") {
  let idx2 = res.indexOf("KBS2");
  if (idx2 > where) {
    if (res[where + 1] === "KBS2") {
      let curEl = res[where];
      res[where] = res[where + 1];
      res[where + 1] = curEl;
      arr += 3;
      where += 1;
    } else {
      arr += 1;
      where += 1;
    }
  } else if (idx2 <= where) {
    if (res[where - 1] === "KBS2") {
      where -= 1;
      arr += 2;
    } else {
      let curEl = res[where];
      res[where] = res[where - 1];
      res[where - 1] = curEl;
      arr += 4;
      where -= 1;
    }
  }
}
console.log(arr);
