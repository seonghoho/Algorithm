function solution(arr, numbers) {
    let res = []
    numbers.forEach((lst) => {
        let exList = arr.slice(parseInt(lst[0])-1,parseInt(lst[1]))
        exList.sort((a,b)=> a-b)
        res.push(exList[parseInt(lst[2])-1])
    })
    return res
}
