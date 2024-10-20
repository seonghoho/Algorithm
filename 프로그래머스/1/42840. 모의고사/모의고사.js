function solution(answers) {
    const lst1 = [1,2,3,4,5]
    const lst2 = [2,1,2,3,2,4,2,5]
    const lst3 = [3,3,1,1,2,2,4,4,5,5]
    let res = [0,0,0]
    for(let i=0; i<answers.length; i++) {
        let curNum = answers[i]
        if (lst1[i%5] === curNum) res[0]++
        if (lst2[i%8] === curNum) res[1]++
        if (lst3[i%10] === curNum) res[2]++
    }
    const max = res.reduce((pre,cur) => pre < cur ? cur : pre)
    let resultArr = []
    res.forEach((elem, index) => 
        { if (elem === max) resultArr.push(index+1)})
    return resultArr
}