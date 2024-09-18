function solution(left, right) {
    let res = 0
    
    for(let i=left; i<= right; i++) {
        let sum = 0
        for (let j=1; j<=i; j++) {
            if (i % j === 0) {
                sum += 1
            }
        }
        sum % 2 ? res -= i : res += i
    }
    return res
}