// 유클리드 호제법
function gcd(a, b) {
    while (b !== 0) {
        let temp = b;
        b = a % b;
        a = temp;
    }
    return a;
}

function lcm(a, b) {
    return (a * b) / gcd(a, b);
}

function solution(arr) {
    return arr.reduce((acc, curr) => lcm(acc, curr));
}