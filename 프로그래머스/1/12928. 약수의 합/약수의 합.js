function solution(n) {
    var count = 0;
    
    for (let i=1; i<n+1; i++) {
        if ((n%i) == 0) {
            count+=i;
        }    
    }
    
    return count;
}