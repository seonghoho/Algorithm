function solution(n, computers) {
    function dfs(node, visited) {
        visited[node] = true
        for(let neighbor=0; neighbor < n; neighbor++) {
            if(computers[node][neighbor] === 1 && !visited[neighbor]) {
                dfs(neighbor, visited)
            }
        }
    }

    const visited = Array(n).fill(false)
    let count = 0
    
    for(let i=0; i<n; i++) {
        if (!visited[i]) {
            dfs(i, visited)
            count++
        }
    }
    return count
}