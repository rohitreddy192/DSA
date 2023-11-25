class Solution:
    def shuffleArray(self, arr, n):
        res = []
        for i in range(n//2):
            res.append(arr[i])
            res.append(arr[i+n//2])
        for i in range(n):
            arr[i] = res[i]
        return arr
        # Your code goes here


#{ 
 # Driver Code Starts
if __name__ == '__main__': 
    
    t=int(input())
    for _ in range(0,t):
        n=int(input())
        a = list(map(int,input().split()))
        ob = Solution()
        ob.shuffleArray(a,n)
        print(*a)
# } Driver Code Ends