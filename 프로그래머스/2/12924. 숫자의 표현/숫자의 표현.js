function solution(n) {
    var cnt=0;
    
    for (let i=1; ((i*(i+1))/2)<=n; i++){       
        if (((n - (i*(i-1)/2)) % i) === 0 ) {
            cnt += 1;
        }
    }
    return cnt
}