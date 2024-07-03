function solution(num_list) {
    var answer = num_list;
    
        if (answer[answer.length-1] > answer[answer.length-2] ) {
            answer.push(answer[answer.length-1] - answer[answer.length-2])
        } else {
            answer.push(answer[answer.length-1]*2) 
        }
        
    return answer;
    
    
}