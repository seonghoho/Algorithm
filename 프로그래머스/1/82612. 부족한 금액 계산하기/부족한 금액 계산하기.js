function solution(price, money, count) {
    let spendMoney = 0
    
    for(let i = 1; i <= count; i++) {
        spendMoney += i * price
    }
    return spendMoney > money ?  spendMoney - money : 0
}