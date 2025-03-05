function solution(elements) {
    const len = elements.length
    const extended = [...elements, ...elements]
    const sums = new Set()
    
    for (let size = 1; size <= len; size++) {
        for (let start = 0; start < len; start++) { 
            let sum = 0
            for (let i = 0; i < size; i++) {
                sum += extended[start + i]
            }
            sums.add(sum)
        }
    }
    
    return sums.size
}
