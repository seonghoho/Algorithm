function solution(A,B){
    A.sort((a,b)=>(a-b))
    B.sort((a,b)=>(b-a))
    var asw = 0

    for (let i=0;i<A.length;i++) {
        asw += A[i]*B[i]
    }
    return asw
}