function solution(s) {
    let flag = true
    //if (isNaN(Number(s)) || (s.length !== 4 && s.length !== 6)) {
    //    flag = false;
    //}
    let lst = s.split('')
    for (let i=0; i<lst.length; i++) {
        if (isNaN(lst[i])) {
            flag = false
        }
    }
    s.length !== 4 && s.length !== 6 ? flag = false : ''
    return flag 
}