class Solution:
    def transitionPoint(self, arr, n): 
        if n==0: return -1
        if arr[0] == 1: return 0
        if arr[-1] == 0: return -1
        
        low = 0
        high = n-1
        ans = -1
        while low<high:
            mid = (low+high)//2
            if arr[mid]<1:
                ans = mid 
                low = mid +1
            else:
                high = mid
        return low if arr[low]==1 else -1
        # Code here








#{ 
 # Driver Code Starts
#driver code
if __name__=='__main__':
    t=int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.transitionPoint(arr, n))

# } Driver Code Ends