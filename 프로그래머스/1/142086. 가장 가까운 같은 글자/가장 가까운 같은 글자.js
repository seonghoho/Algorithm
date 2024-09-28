// function solution(s) {
//     let lst = []
//     let res = []
    
//     s.split('').forEach((elem) => {
//         if (lst.find((e) => e === elem)) {
//             lst.push(elem)
            
//             for(let i=lst.length-1; i>0; i--) {
//                 if (elem === lst[i]) {
//                     res.push(i)
//                     return
//                 }
//             }
            
            
//         } else {
//             res.push(-1)
//             lst.push(elem)
//         }
//     })
//     return res    
// }

function solution(s) {
    let lst = {};  // 문자의 마지막 위치를 저장하는 객체
    let res = [];
    
    s.split('').forEach((elem, idx) => {
        if (lst.hasOwnProperty(elem)) {  // 문자가 이전에 등장했는지 확인
            res.push(idx - lst[elem]);  // 현재 인덱스와 마지막 등장 인덱스의 차이 저장
        } else {
            res.push(-1);  // 처음 등장한 문자는 -1
        }
        lst[elem] = idx;  // 문자의 마지막 등장 위치 업데이트
    });
    
    return res;
}
