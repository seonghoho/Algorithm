function solution(num) {
     if (num === 1) {
         return 0
     } else {
    let res = num;
    let cnt = 0;
    
    while (res !== 1) {
        if (cnt > 500) {
            cnt= -1; 
            break
        } else {
        if (res % 2 === 0) {
            res /= 2;
            cnt += 1;
        } else {
            res *= 3;
            res += 1;
            cnt += 1;           
        }}
    }
    return cnt
     }
}