function solution(t, p) {
    let pLen = p.length
    let cnt = 0
    for(let i = 0; i<=t.length - pLen; i++) {
        t.slice(i,i+pLen) <= p ? cnt++ : ''
    }
    return cnt
}