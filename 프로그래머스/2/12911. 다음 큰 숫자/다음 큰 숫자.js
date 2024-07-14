function solution(n) {
    // 2진법으로 변환 => forEach로 1 갯수 파악 => n부터 for문 사용해서 숫자에 1갯수 세서 n과 같으면 break
    let arr = n.toString(2).split('');
    // forEach로 1 갯수 파악
    let countOne = 0;
    arr.forEach((i) => {
        if (i === '1') {
        countOne += 1;    
    }
    })
    // n부터 for문 사용해서 숫자에 1갯수 세서 n과 같으면 break
    let newCount = 0;
    let newNumber = n+1;
    
    while(1) {
        let newArr = newNumber.toString(2).split('');
        newArr.forEach((i) => {
            if (i === '1') {
                newCount += 1;
            }
        })
        
        if (newCount === countOne) {
            break;
        } else {
            newCount = 0;
            newNumber += 1;
        }
    }
    
    return newNumber;
}