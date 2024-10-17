function solution(cards1, cards2, goal) {
    let lst1 = cards1
    let lst2 = cards2
    for(let word of goal) {
        if(lst1[0] === word) {
            lst1.shift()
        } else if (lst2[0] === word) {
            lst2.shift()
        } else {
            return 'No'
        }
    }
    return 'Yes'
}