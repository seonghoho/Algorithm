function solution(n) {

    var sum = 0;
    (n+'').split('').map(num => (sum += parseInt(num)));
    return sum;
}