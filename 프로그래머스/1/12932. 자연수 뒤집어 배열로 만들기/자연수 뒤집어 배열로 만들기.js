function solution(n) { 
    return (n+'').split('').map(i => (parseInt(i))).reverse();
}