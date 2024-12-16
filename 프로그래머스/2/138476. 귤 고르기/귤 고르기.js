function solution(k, tangerine) {
    const countMap = new Map()
    
    for (let size of tangerine) {
        countMap.set(size, (countMap.get(size) || 0) + 1)
    }
    
    const sortedCounts = Array.from(countMap.values()).sort((a, b) => b - a)
    
    let total = 0
    let types = 0

    for (let count of sortedCounts) {
        total += count
        types++
        if (total >= k) {
            break
        }
    }

    return types
}

