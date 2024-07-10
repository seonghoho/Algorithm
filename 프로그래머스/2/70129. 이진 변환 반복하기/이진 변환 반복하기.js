function solution(s) {
    var num = 0;
    var zero = 0;
    var sol = s;
    
    while (sol !=='1') {
    num += 1;
        
    // 배열로 만들기
    var splitSol = sol.split('');
        
    // 1, 0 갯수 초기화
    var one = 0;
    var z = 0;
        
    // s에 1, 0 갯수 카운트
    splitSol
        
    splitSol.forEach(n => {
        if (n === '1') {
            one += 1
        } else if (n === '0') {
            z += 1
        }
    })
        
    zero += z;
    sol = one.toString(2);
        
    }
    return [num, zero]
}