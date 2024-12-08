function solution(n) {
    for(let i=2; i<=Math.sqrt(n); i++) {
        if (i**2 === n) return 1
        continue
    }
    return 2
}