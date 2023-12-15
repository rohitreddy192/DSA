#User function Template for python3

class Solution:
    def findPath(self, m, n):
        def solve(i,j,ds,ans,visited):
            if i==n-1 and j==n-1:
                t = "".join(ds)
                ans.append(t)
                return 
            if i<0 or j<0 or i>=n or j>=n:
                return 
            visited[i][j] = True
            if i<n-1 and m[i+1][j] == 1 and not visited[i+1][j]:
                ds.append("D")
                solve(i+1,j,ds,ans,visited)
                ds.pop()
            if i>0 and m[i-1][j] == 1 and not visited[i-1][j]:
                ds.append("U")
                solve(i-1,j,ds,ans,visited)
                ds.pop()
            if j<n-1 and m[i][j+1] == 1 and not visited[i][j+1]:
                ds.append("R")
                solve(i,j+1,ds,ans,visited)
                ds.pop()
            if j>0 and m[i][j-1] == 1 and not visited[i][j-1]:
                ds.append("L")
                solve(i,j-1,ds,ans,visited)
                ds.pop()
            visited[i][j] = False
        if m[0][0] == 0: return []
        ans = list()
        visited = [[False for i in range(n)] for j in range(n)]
        solve(0,0,[],ans,visited)
        return sorted(ans)
                
        # code here





#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        
        matrix = [[0 for i in range(n[0])]for j in range(n[0])]
        k=0
        for i in range(n[0]):
            for j in range(n[0]):
                matrix[i][j] = arr[k]
                k+=1
        ob = Solution()
        result = ob.findPath(matrix, n[0])
        result.sort()
        if len(result) == 0 :
            print(-1)
        else:
            for x in result:
                print(x,end = " ")
            print()
# } Driver Code Ends