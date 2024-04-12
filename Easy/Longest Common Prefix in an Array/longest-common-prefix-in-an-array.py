#User function Template for python3

class Solution:
    def longestCommonPrefix(self, arr, n):
        arr.sort()
        a = arr[0]
        for i in range(len(a)):
            for j in range(len(arr)):
                if arr[j][i] != a[i]:
                    return a[:i] if len(a[:i])!=0 else -1
        return a
        # code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        n = int(input())
        arr = [x for x in input().strip().split(" ")]
        
        ob=Solution()
        print(ob.longestCommonPrefix(arr, n))
# } Driver Code Ends