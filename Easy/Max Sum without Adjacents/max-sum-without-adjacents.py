#User function Template for python3
class Solution:
	
	def findMaxSum(self,arr, n):
	    
	    dp = [0]*n
	    dp[0] = arr[0]
	    maxVal = arr[0]
	    for i in range(1,n):
	        take = arr[i]
	        if i>=2:
    	        take = arr[i] + dp[i-2]
	        nottake = dp[i-1]
	        dp[i] = max(take,nottake)
	        maxVal = max(maxVal,dp[i])
	    return maxVal
	    """
	    def solve(i,dp):
	        if i<0: return 0
	        if i==0: return arr[0]
	        if dp[i]!=-1: return dp[i]
	        
	        take = arr[i]+solve(i-2,dp)
	        nottake = 0 + solve(i-1,dp)
	        
	        dp[i] = max(take, nottake)
	        return dp[i]
	    dp = [-1 for i in range(n)]
	    return solve(n-1,dp)
		"""# code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3




if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.findMaxSum(arr, n)
        print(ans)
        tc -= 1

# } Driver Code Ends