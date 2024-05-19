#User function Template for python3

class Solution:
    def longestPalindrome(self, S):
        def isPalindrome(a):
            return a==a[::-1]
        
        n = len(S)
        maxLen = 0
        res = ""
        for i in range(n):
            for j in range(i,n):
                if isPalindrome(S[i:j+1]) and maxLen<(j-i+1):
                    maxLen = j-i+1
                    res = S[i:j+1]
        
        return res
        # code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        
        S = input().strip()
        ob=Solution()
        print(ob.longestPalindrome(S))
# } Driver Code Ends