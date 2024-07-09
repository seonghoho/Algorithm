function solution(s) {
    var list = s.split(' ')
    var res = []
    for (let i=0; i<list.length; i++) {
        
        var first = []
        
        if (list[i] !== '' && isNaN(list[i][0])) {
            first.push(list[i][0].toUpperCase());
            first.push(list[i].slice(1,list[i].length).toLowerCase());
            res.push(first.join(''));
            
        } else {
            res.push(list[i].toLowerCase());
        }
    }
    
    return res.join(' ')
}