function solution(s) {
    let count = 0
    let firstChar = ''
    let firstCount = 0
    let otherCount = 0

    for (let i = 0; i < s.length; i++) {
        if (firstCount === otherCount) {
            count++
            firstChar = s[i]
            firstCount = 0
            otherCount = 0
        }

        if (s[i] === firstChar) {
            firstCount++
        } else {
            otherCount++
        }
    }
    return count
}