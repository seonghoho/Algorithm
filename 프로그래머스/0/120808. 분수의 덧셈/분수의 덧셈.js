function solution(numer1, denom1, numer2, denom2) {
    let num1 = numer1 * denom2
    let num2 = numer2 * denom1
    let den = denom1 * denom2
    let num = num1 + num2

    function gcd(a, b) {
        while (b !== 0) {
            let temp = b
            b = a % b
            a = temp
        }
        return a
    }

    let divisor = gcd(num, den)
    num /= divisor
    den /= divisor

    return [num, den]
}