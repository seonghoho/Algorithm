function solution(seoul) {
    let where = 0;
    seoul.forEach((name,index) => {
        if(name === 'Kim') {
            where = index;
        }
    })
    return '김서방은 '+where+'에 있다'
}