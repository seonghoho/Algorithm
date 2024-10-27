function solution(n, m, section) {
    let res = 0
    let i = 0
    while (i < section.length) {
        res++
        let current = section[i]
        while (i < section.length && section[i] < current + m) {
            i++;
        }
    }
    return res
}