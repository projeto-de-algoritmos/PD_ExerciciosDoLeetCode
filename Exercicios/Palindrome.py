class Solution(object):
    def partition(self, s):
        n = len(s)
        isPalindrome = [[False] * n for _ in range(n)]
        dp = [[] for _ in range(n)]

        for i in range(n):
            for j in range(i + 1):
                if s[j:i + 1] == s[j:i + 1][::-1]:
                    isPalindrome[j][i] = True

        for i in range(n):
            for j in range(i + 1):
                if isPalindrome[j][i]:
                    if j == 0:
                        dp[i].append([s[j:i + 1]])
                    else:
                        for part in dp[j - 1]:
                            dp[i].append(part + [s[j:i + 1]])

        return dp[-1]