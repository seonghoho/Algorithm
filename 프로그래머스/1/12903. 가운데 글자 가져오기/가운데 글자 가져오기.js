function solution(s) {
    let lst = (s+'').split('')
    let lstLength = lst.length
    if (lstLength % 2) {
        return lst[parseInt(lstLength / 2)]
    } else {
        let res = [lst[lstLength/2 -1], lst[lstLength/2]]
        return res.join('')
    }
    
}