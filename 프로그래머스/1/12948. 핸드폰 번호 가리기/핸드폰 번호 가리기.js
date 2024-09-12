function solution(phone_number) {
    
    // let blindNums = new Array(phone_number.length-4).fill('*').join('')
    // let lastNums = phone_number.slice(phone_number.length-4, phone_number.length)
    // return blindNums + lastNums
    
    return '*'.repeat(phone_number.length-4) + phone_number.slice(-4)
    
}