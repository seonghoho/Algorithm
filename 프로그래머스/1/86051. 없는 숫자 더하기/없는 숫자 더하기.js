function solution(numbers) {
    let lst = [1,2,3,4,5,6,7,8,9]
    let arr = new Set()

    numbers.forEach(n => {
        if (lst.find(a => a === n)) {
            arr.add(n)
        }
    })
    
    let sum = 0;
    
    for(let i=1; i<10; i++) {
        arr.has(i) ? '' : sum += i 
    }
    return sum    
}