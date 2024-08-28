function solution(my_string, k) {
    let res = []
    for(let i=0;i<k;i++) {
        res.push(my_string)
    }
    return res.join('');
}