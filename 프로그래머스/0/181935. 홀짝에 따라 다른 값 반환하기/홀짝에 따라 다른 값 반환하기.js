function solution(n) {
    let res = 0   
    
    if (n%2) {
        for(let i=1; i<=n; i++) {
            if (i%2 !== 0) {
                res += i
            }
        }
    } else {
        for(let i=1; i<=n; i++) {
            if (i%2 === 0) {
                res += i*i
            }
        }
    }
    
    
    return res
}