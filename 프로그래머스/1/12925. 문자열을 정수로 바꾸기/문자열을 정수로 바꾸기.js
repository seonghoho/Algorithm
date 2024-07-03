function solution(s) {
    var answer = 0;
    var number = [];
    
    if (s[0] == '-') {
        number.push('-')
        
        for (let i=1; i<s.length;i++){
            number.push(Number(s[i]))
        }
    } else if (s[0] == '+') {
        for (let i=1; i<s.length;i++){
            number.push(Number(s[i]))
        }
    } else {
        for (let i=0; i<s.length;i++) {
            number.push(s[i])
        }
    }
    
    answer = Number(number.join(''))
    return answer;
}