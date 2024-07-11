function solution(brown, yellow) {
    // b가 8이상, y가 1이상으로 시작해서 한 면 최소 길이는 3
    // x*y = bro+yel => y = (bro+yel)/x 임
    for (var y = 3; y<= (brown + yellow)/y; y++) {
        // 저 값이 x식이다
        var x = Math.floor((brown + yellow)/y);
        // 테두리 내부에 노란색이라 -2씩 한 수와 일치한다
        if ((x-2) * (y-2) === yellow) {
            break;
        } 
    }
    return [x,y]
}