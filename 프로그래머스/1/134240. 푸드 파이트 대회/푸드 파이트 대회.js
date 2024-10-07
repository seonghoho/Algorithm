function solution(food) {
    let res = ''
    let part = ''
    let devideTwo = food.map((el) => (Math.floor(el/2)))
    for(let i=1; i<food.length; i++) {
        if (devideTwo[i] !== 0) {
            let cnt = 0
            while (cnt < devideTwo[i]) {
                part += i
                cnt++
            }
        }
    }
    res = part + 0 + part.split('').reverse().join('')
    return res
}