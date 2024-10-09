function solution(strings, n) {
    strings.sort()
    strings.sort((a,b) => {
        let numA = a[n].toUpperCase()
        let numB = b[n].toUpperCase()
        if (numA < numB) {
            return -1
        }
        if (numA > numB) {
            return 1
        }
        if (numA === numB) {
           return 0
        }
    })
    
    return strings
}