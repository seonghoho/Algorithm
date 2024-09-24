function solution(s) {
    let lst = s.split(' ')
    let newLst = []
    for (let elem in lst) {
        let word = lst[elem].split('')
        let newWord = ''
        for (let spel in word) {
            newWord += spel % 2 ? word[spel].toLowerCase() : word[spel].toUpperCase()
        }
        newLst.push(newWord)
    }
    return newLst.join(' ')
}