function solution(a, b, n) {
    let res = 0;
    let total = n; 
    
    while (total >= a) {  
        let sale = Math.floor(total / a); 
        let newCola = sale * b;  
        res += newCola; 
        total = total % a + newCola;  
    }
    
    return res; 
}
