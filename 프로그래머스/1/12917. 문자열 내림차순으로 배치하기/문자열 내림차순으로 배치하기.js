function solution(s) {
    let lst = s.split('')
    lst.sort()
    return lst.reverse().join('')
}