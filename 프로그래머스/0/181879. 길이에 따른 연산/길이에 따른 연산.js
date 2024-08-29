function solution(num_list) {
    let res = 0;
    if (num_list.length > 10) {
        num_list.forEach((elem)=> {
            res += elem;
        })
    } else {
        res = 1
         num_list.forEach((elem)=> {
             console.log('들어는 옴?')
            res *= elem;
        })
    }
    return res;
}