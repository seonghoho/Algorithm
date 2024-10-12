function solution(k, score) {
    let lst = []
    let res = []
    for(let i = 0; i<score.length; i++) {
        lst.push(score[i])
        lst.sort((a,b) => b-a)
        if (lst.length >k) lst.pop()
        res.push(Math.min(...lst))
    }
    return res
}