function solution(babbling) {
    const validWords = ['aya', 'ye', 'woo', 'ma']
    let count = 0
    for (let word of babbling) {
        let previous = ''
        let isValid = true
        while (word.length > 0) {
            let matched = false;
            for (let valid of validWords) {
                if (word.startsWith(valid) && previous !== valid) {
                    word = word.slice(valid.length)
                    previous = valid
                    matched = true
                    break
                }
            }
            if (!matched) {
                isValid = false
                break
            }
        }
        if (isValid) count++
    }
    return count
}
