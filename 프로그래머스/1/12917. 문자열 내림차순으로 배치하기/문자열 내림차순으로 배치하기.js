function solution(s) {
    let lst = s.split('')
    lst.sort((a,b)=> b.charCodeAt(0) - a.charCodeAt(0))
    return lst.join('')
}