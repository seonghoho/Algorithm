function solution(s, n) {
   let lst = s.split('')  
   
   let res = []
   lst.forEach((el) => {
       let num = el.charCodeAt()
       if (num === 32) {
           res.push(String.fromCharCode(num))
       } else if (97 <= num && num <= 122) {
           res.push(String.fromCharCode((num + n - 97) % 26 + 97))
       } else if (65 <= num && num <= 90) {
           res.push(String.fromCharCode((num + n - 65) % 26 + 65))
       }
   })
    return res.join('')
}