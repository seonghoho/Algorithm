function solution(nums) {
    let setArr = new Set(nums)
    let len = nums.length/2
    return setArr.size > len ? len : setArr.size 
}