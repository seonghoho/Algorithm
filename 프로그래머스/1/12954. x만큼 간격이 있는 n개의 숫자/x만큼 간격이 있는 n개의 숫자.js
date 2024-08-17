function solution(x, n) {
    let lst = new Array
    let num = x
    for(let i=0; i<n; i++) {
        lst.push(num)
        num += x
    }
    return lst
}