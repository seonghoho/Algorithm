function solution(n) {
    let x = parseInt(n)
    let res = 0
    for(let i=1; i<x; i++) {
        if (n%i === 1) {
            return res = i
            break
        }
    }
    return console.log(res)
}