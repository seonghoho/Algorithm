function solution(n, m) {
    let min = Math.min(n,m)
    let max = Math.max(n,m)
    let small,big = 0
    
    for(let i=1; i<=min; i++) {
        if (min%i===0 && max%i===0) {
            small = i
        }
    }
    big = small * (min/small) * (max/small)
    return [small,big]
}