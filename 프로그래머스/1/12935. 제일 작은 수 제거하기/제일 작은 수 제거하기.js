function solution(arr) {
    if (arr.length === 1) {
        return [-1]
    } else {
    let lst = []
    let minNum = Math.min(...arr)
    arr.forEach((el) => {
        minNum !== el ? (lst.push(el)) : ''
    })
    return lst
    }
    
}