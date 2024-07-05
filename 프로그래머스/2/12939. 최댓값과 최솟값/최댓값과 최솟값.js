function solution(s) {
    var arr = s.split(' ').map(n => parseInt(n))
    
    var max = -Infinity;
    var min = Infinity;
    
    arr.forEach(n => {
        if (max < n) {
            max = n
        }
        if (min > n) {
            min = n
        }
    })
    
    return (min + ' ' + max)
} 