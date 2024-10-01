function solution(arr) {
//   let res = [arr[0]]
//   for(let i=1; i<arr.length; i++) {
//       arr[i] === res[res.length-1] ? '' : res.push(arr[i])
//   }
//    return res
    return arr.filter((num,index) => num !== arr[index+1])
}