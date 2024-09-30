function solution(numbers) {
    let newSet = new Set()
    for(let i=0; i< numbers.length-1; i++) {
        for(let j=i+1; j< numbers.length; j++) {
            newSet.add(numbers[i]+ numbers[j])
        }
    }
    // let resArr = new Array()
    // newSet.forEach((num) => {
    //     resArr.push(num)
    // })
    let resArr = [...newSet]
    return resArr.sort((a,b) => a-b)
}