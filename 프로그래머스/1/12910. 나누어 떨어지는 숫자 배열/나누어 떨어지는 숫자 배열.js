function solution(arr, divisor) {
    let res = arr.filter((num) => num % divisor === 0).sort((a,b) => a-b)
    
    return res.length ? res : [-1]
}