function solution(n) {
    var arr = String(n).split('');
    var sum = 0;
    for (let i=0; i<arr.length; i++) {
        sum += Number(arr[i]);
    }
    return sum;
}