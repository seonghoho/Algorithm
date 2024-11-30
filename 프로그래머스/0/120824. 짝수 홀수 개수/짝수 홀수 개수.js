function solution(num_list) {
    const cnt = num_list.filter((el)=>el%2).length
    return [num_list.length-cnt, cnt]
}