function solution(a, b) {
    let res = 0;
    let start = Math.min(a,b)
    let finish = Math.max(a,b)
    if (a === b) {
        return a
    } else {
    for(let i=start;i<=finish;i++) {
        res+= i
    }
    return res
    }
}