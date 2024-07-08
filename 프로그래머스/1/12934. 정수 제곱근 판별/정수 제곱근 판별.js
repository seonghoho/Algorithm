function solution(n) {
    var i = 0
    while (i**2 < n) {
        if ((i**2) === n) {
            break
        } else if (i**2 > n) {
            break
        } else {
            i+=1; 
        }
    }
    if ((i**2) === n) {
            return ((i+1)**2)
        } else if (i**2 > n) {
            return (-1)
        }
}