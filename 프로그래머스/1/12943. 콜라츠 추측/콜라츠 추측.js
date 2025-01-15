function solution(num) {
    let n = num
    let cnt = 0
    while (n !== 1 && cnt !== 500) {
        n % 2 == 0 ? n = n / 2 : n = n * 3 + 1
        cnt += 1
    }
    return n == 1 ? cnt < 500 ? cnt : -1 : -1
}