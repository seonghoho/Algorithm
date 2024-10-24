function solution(n) {
    let arr = new Array(n+1).fill(1)
    arr[0] = arr[1] = 0
    
    for (let i = 2; i * i <= n; i++) {  
        if (arr[i] === 1) {  
            for (let j = i * i; j <= n; j += i) {  
                arr[j] = 0;
            }
        }
    }
    return arr.reduce((cur, total) => cur + total, 0)
}