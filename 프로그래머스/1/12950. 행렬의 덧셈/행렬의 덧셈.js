function solution(arr1, arr2) {
    let lst = []
    for(let i=0; i<arr1.length; i++) {
        let lst2 = []
        for(let j=0; j<arr1[0].length; j++) {
        lst2.push(parseInt(arr1[i][j]) + parseInt(arr2[i][j]))
        }
        lst.push(lst2)
    }
    return lst
}