function solution(nums) {
    let res = 0
    for(let i=0; i<nums.length-2; i++) {
        for(let j=i+1; j<nums.length-1; j++) {
            for(let k=j+1; k<nums.length; k++) {
                let num = nums[i]+ nums[j] + nums[k]
                let flg = 0
                for(let l=2; l*2 <=num; l++) {
                    if (num%l === 0) flg++
                }
                if (!flg) res++
            }
        }
    }
    return res
}