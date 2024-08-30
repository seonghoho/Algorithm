function solution(arr) {
    let res = []
    arr.forEach((elem) => {
        if (elem >= 50 && elem%2 === 0) {
            res.push(elem/2)
        } else if (elem < 50 && elem%2 !==0) {
            res.push(elem*2)
        } else {
            res.push(elem)
        }
    })
    return res
}