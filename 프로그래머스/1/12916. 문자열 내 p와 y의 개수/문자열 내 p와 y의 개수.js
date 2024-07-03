function solution(s){
    var answer = true;
    
    var num_p = 0
    var num_y = 0
    
    for (let i=0; i< s.length; i++) {
        if (s[i] == 'p' || s[i] == 'P') {
            num_p += 1;
        } else if (s[i] == 'y' || s[i] == 'Y') {
            num_y += 1;
        }
    }

    if (num_p != num_y) {
        answer = false
    }
    return answer;
}