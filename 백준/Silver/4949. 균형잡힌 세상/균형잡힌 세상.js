const input = require("fs")
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split("\n");

input.pop();

input.forEach((lst) => {
  let arr = [];
  let result = true;

  lst.split("").forEach((word) => {
    if (word === "(") {
      arr.push("(");
    } else if (word === "[") {
      arr.push("[");
    } else if (word === "]") {
      if (arr.length > 0 && arr[arr.length - 1] === "[") {
        arr.pop();
      } else {
        result = false;
      }
    } else if (word === ")") {
      if (arr.length > 0 && arr[arr.length - 1] === "(") {
        arr.pop();
      } else {
        result = false;
      }
    }
    // console.log(word);
  });
  //   console.log(arr);

  if (arr.length !== 0) {
    result = false;
  }
  console.log(result ? "yes" : "no");
});
