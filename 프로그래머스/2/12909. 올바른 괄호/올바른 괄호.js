function solution(s){
    var n=0;
    
    for(let i=0; i<s.length;i++){
    s[i] === '(' ? (n += 1) : (n -=1)
        
    if (n < 0) {
        break
    }
       
}
   return n == 0 ? true : false
    
}