function solution(n, arr1, arr2) {
    let lst = []
    let word1 = []
    let word2 = []
    let res = []
    for (let i=0; i<n; i++) {
        let num1 = arr1[i].toString(2)
        let zero1 = new Array(n-num1.split('').length).fill('0').join('')
        word1.push((zero1 + num1).split(''))
        let num2 = arr2[i].toString(2)
        let zero2 = new Array(n-num2.split('').length).fill('0').join('')
        word2.push((zero2 + num2).split(''))
    }
    for (let i=0; i<word1.length; i++) {
        let secret = ''
        for(let j=0; j<n; j++) {
            let isBlock = false
            word1[i][j] == 1 || word2[i][j] == 1 ? isBlock = true : ''
            isBlock ? secret+= '#' : secret+= ' '
        }
        res.push(secret)
    }
    return res
}