const input = require("fs")
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split("\n")
  .map((num) => num.split(" ").map(Number));

const [N, M, V] = input.shift();

// 어느 선이 어느 선으로 연결되는지 인접 리스트 구하는 로직
const graph = {};

// 그래프 초기화
for (let i = 1; i <= N; i++) {
  graph[i] = [];
}

input.forEach(([from, to]) => {
  graph[from].push(to);
  graph[to].push(from);
});

// 각 노드의 인접 리스트 정렬
for (let key in graph) {
  graph[key].sort((a, b) => a - b);
}

// 방문한 곳 순서대로 저장하는 리스트
let dfs_list = new Array();

// 재귀를 사용한 dfs 함수
const dfs = (lst, start, visited = new Set()) => {
  if (visited.has(start)) return;

  visited.add(start);
  dfs_list.push(start);

  for (const next of lst[start]) {
    dfs(lst, next, visited);
  }
};

// dfs 실행
dfs(graph, V);

// dfs 순서대로 출력
console.log(dfs_list.join(" "));

// bfs 목록 선언
let bfs_list = new Array();

// bfs
const bfs = (graph, start) => {
  const visited = new Set();
  const queue = [start];

  while (queue.length > 0) {
    const node = queue.shift();

    if (!visited.has(node)) {
      visited.add(node);
      bfs_list.push(node);

      for (const next of graph[node]) {
        queue.push(next);
      }
    }
  }
};

bfs(graph, V);

console.log(bfs_list.join(" "));
