#User function Template for python3
class Solution:

	def nextGreatest(self,arr, n):
	    temp = -1
	    for i in range(n-1,-1,-1):
	        t = arr[i]
	        arr[i] = temp
	        if temp<t:
	            temp = t
	    
		# code  here


#{ 
 # Driver Code Starts
#Initial Template for Python 3



if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ob.nextGreatest(arr, n)
        for x in arr:
            print(x, end=" ")
        print()
        tc -= 1

# } Driver Code Ends