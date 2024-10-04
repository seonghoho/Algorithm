const input = require("fs").readFileSync("/dev/stdin").toString().trim();

let lst = [
  ["*", "*", "*", "*", "*"],
  ["*", " ", " ", " ", " "],
  ["*", " ", "*", "*", "*"],
  ["*", " ", "*", " ", "*"],
  ["*", " ", "*", " ", "*"],
  ["*", " ", " ", " ", "*"],
  ["*", "*", "*", "*", "*"],
];

if (Number(input) > 2) {
  let width = 5;
  let cnt = 1;

  while (cnt < Number(input) - 1) {
    let res = [];

    let startList = Array(width + cnt * 4).fill("*");
    res.push(startList);

    let secondList = Array(width - 1 + cnt * 4).fill(" ");
    secondList.unshift("*");
    res.push(secondList);

    for (let i = 0; i < lst.length; i++) {
      if (i === 0) {
        let list = ["*", " "];
        let newList = list.concat(lst[i]);
        newList.push("*");
        newList.push("*");
        res.push(newList);
      } else {
        let exList = ["*", " "];
        let newList = exList.concat(lst[i]);
        newList.push(" ");
        newList.push("*");
        res.push(newList);
      }
    }

    let backTwoList = Array(width - 2 + cnt * 4).fill(" ");
    backTwoList.unshift("*");
    backTwoList.push("*");
    res.push(backTwoList);

    res.push(startList);

    lst = res;

    cnt++;
  }
}

if (Number(input) === 1) {
  console.log("*");
} else {
  for (let i = 0; i < lst.length; i++) {
    if (i === 1) {
      console.log("*");
    } else {
      console.log(lst[i].join(""));
    }
  }
}
