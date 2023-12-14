#Your task is to complete this function
#Your should return the required output
class Solution:
    def maxLen(self, n, arr):
        hm = {}
        sum = 0
        maxLen = 0
        for i in range(n):
            sum += arr[i]
            if sum == 0:
                maxLen = max(maxLen,i+1)
            if sum in hm:
                maxLen = max(maxLen,i-hm[sum])
            else:
                hm[sum] = i
        return maxLen
        #Code here


#{ 
 # Driver Code Starts
if __name__=='__main__':
    t= int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.maxLen(n ,arr))
# Contributed by: Harshit Sidhwa
# } Driver Code Ends