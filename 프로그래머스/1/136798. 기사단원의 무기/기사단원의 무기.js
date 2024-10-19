function solution(number, limit, power) {
    let res = 0
    for(let i=1; i<=number; i++) {
        let num = 0
        for(let j=1;j*j<=i; j++) {
            if(i%j === 0) {
                num++
                if (j !== i/j) num++
            }
        }
        if (num > limit) num = power
        res += num
    }
    return res
}