function solution(d, budget) {
    d.sort((a,b) => a-b)
    let money = budget
    let cnt = 0
    for(let i=0; i<d.length; i++) {
        if (money >= d[i]) {
            cnt++
            money -= d[i]
        } else {
            break
        }
    }
    return cnt
}