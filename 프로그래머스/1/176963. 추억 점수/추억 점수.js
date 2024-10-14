function solution(name, yearning, photo) {
    let mapNumbers = new Map()
    for(let i=0; i<name.length; i++) {
        mapNumbers.set(name[i], yearning[i])
    }
    let res = []
    photo.forEach((lst) => {
        let score = 0
        lst.forEach((el) => {
            if (mapNumbers.get(el)) score += mapNumbers.get(el)
        })
        res.push(score)
    })
    return res
}