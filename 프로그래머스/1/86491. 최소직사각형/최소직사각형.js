function solution(sizes) {
    let maxNum = 0
    let minNum = 0
    
    sizes.forEach((elem) => {
        let maxElem = Math.max(...elem)
        let minElem = Math.min(...elem)
        maxNum < maxElem ? maxNum = maxElem : ''
        minNum < minElem ? minNum = minElem : ''
    })
    return maxNum * minNum    
}