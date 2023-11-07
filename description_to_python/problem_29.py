

def numDecodings(s):
    n = len(s)
    dp = [0] * (n + 1)
    dp[0] = 1
    for i in range(1, n + 1):
        if s[i - 1] != "0":
            dp[i] += dp[i - 1]
        if i != 1 and s[i - 2] == "1" or (s[i - 2] == "2" and s[i - 1] <= "6"):
            dp[i] += dp[i - 2]
    return dp[n]