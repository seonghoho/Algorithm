const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

let input = [];

rl.on('line', function (line) {
    input = [line];
    let res = []
    let lst = input[0].split('')
    lst.forEach((elem) => {
        elem === elem.toUpperCase() ? res.push(elem.toLowerCase()) : res.push(elem.toUpperCase())
    })
    console.log(res.join(''))
    
}).on('close',function(){
    str = input[0];
});