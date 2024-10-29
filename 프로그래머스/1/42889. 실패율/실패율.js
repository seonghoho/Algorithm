function solution(N, stages) {
    let failureRates = []
    let totalPlayers = stages.length
    
    for (let i=1; i <= N; i++) {
        let stopped = stages.filter(stage => stage === i).length
        
        let failureRate = 0
        if (totalPlayers > 0) {
            failureRate = stopped / totalPlayers
        }
    failureRates.push([i, failureRate])
    
    totalPlayers -= stopped
        
    }    
    failureRates.sort((a,b)=> b[1]-a[1] || a[0]-b[0])
    return failureRates.map((el)=> el[0])
}