function solution(s) {
    let res = []
    let word = []
    
     s.split('').forEach((elem) => {
        if (!isNaN(elem)) {
            res.push(elem);
        } else {
            word.push(elem);
            let num = word.join('');
            
            if (num === 'zero') {
                res.push(0);
                word = [];
            } else if (num === 'one') {
                res.push(1);
                word = [];
            } else if (num === 'two') {
                res.push(2);
                word = [];
            } else if (num === 'three') {
                res.push(3);
                word = [];
            } else if (num === 'four') {
                res.push(4);
                word = [];
            } else if (num === 'five') {
                res.push(5);
                word = [];
            } else if (num === 'six') {
                res.push(6);
                word = [];
            } else if (num === 'seven') {
                res.push(7);
                word = [];
            } else if (num === 'eight') {
                res.push(8);
                word = [];
            } else if (num === 'nine') {
                res.push(9);
                word = [];
            }
        }
    })
    return Number(res.join(''))
}