function solution(num_list, n) {
    let arr = []
    for(let i=n-1; i<num_list.length; i++) {
        arr.push(num_list[i])
    }
    return arr
}