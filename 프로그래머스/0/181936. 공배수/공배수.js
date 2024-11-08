function solution(number, n, m) {
    let flg = true
    if (number % n) flg = false
    if (number % m) flg = false
    return flg ? 1 : 0
}