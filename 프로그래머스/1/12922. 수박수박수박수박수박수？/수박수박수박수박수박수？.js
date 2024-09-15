function solution(n) {
    // let str = ''
    // for(let i=0; i< Math.floor(n/2); i++) {
    //         str += '수박'
    //     }
    // return n%2 ? str+'수' : str
    
    return ('수박').repeat(n).slice(0,n)
}