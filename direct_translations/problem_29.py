

def numDecodings(s):
    if s is None or len(s) == 0 or s[0] == '0':
        return 0
    n = len(s)
    dp = [1, 1 if s[0] != '0' else 0]
    for i in range(2, n+1):
        first = int(s[i-1:i])
        second = int(s[i-2:i])
        if first >= 1 and first <= 9:
            dp.append(dp[i-1])
        if second >= 10 and second <= 26:
            dp[i] += dp[i-2]
    return dp[n]