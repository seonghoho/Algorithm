function solution(x) {
    let number = x.toString().split('').map(Number).reduce((res,current) => res + current,0)

    return !(x % number)
}