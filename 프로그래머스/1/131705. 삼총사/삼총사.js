function solution(number) {
    let cnt = 0
    for(let i=0; i<number.length-2; i++) {
        for(let j=i+1; j<number.length-1; j++) {
            for(let k=j+1; k<number.length; k++) {
                number[i] + number[j] + number[k]  ? '' : cnt++
            }
        }
    }
    return cnt
}