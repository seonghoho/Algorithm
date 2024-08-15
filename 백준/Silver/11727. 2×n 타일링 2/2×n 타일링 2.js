const input = parseInt(require("fs").readFileSync("dev/stdin").toString());

const tile = (n) => {
  if (n === 1) return 1;
  if (n === 2) return 3;

  const dp = new Array(n + 1).fill(0);
  dp[1] = 1;
  dp[2] = 3;

  for (let i = 3; i <= n; i++) {
    dp[i] = (dp[i - 1] + 2 * dp[i - 2]) % 10007;
  }
  return dp[n];
};

console.log(tile(input));
