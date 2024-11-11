function solution(num_list) {
    let hol = ''
    let zzak = ''
    num_list.forEach((el)=> {
        (el%2) ? zzak+=el : hol+=el 
    })
    return Number(hol) + Number(zzak)
}