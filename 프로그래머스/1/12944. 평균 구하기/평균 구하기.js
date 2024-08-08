function solution(arr) {
    let sum = 0;
    let cnt = 0
    arr.forEach(n => {
        sum += n;
        cnt += 1;
    })
    return sum/cnt;
}