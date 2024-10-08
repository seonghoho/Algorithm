function solution(num_list) {
    let gob = num_list.reduce((lst,curEl) => lst*curEl,1)
    let hab = num_list.reduce((lst,curEl) => lst+curEl,0)
    return (gob < hab*hab) ? 1 : 0
}