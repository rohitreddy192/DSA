#User function Template for python3

class Solution:
    def sort012(self,arr,n):
        
        left, mid,right = 0,0, n-1
        
        while mid<=right:
            if arr[mid] == 0:
                arr[left], arr[mid] = arr[mid], arr[left]
                left += 1
                mid += 1
            elif arr[mid] == 1:
                mid += 1
            elif arr[mid]==2:
                arr[right], arr[mid] = arr[mid], arr[right]
                right -= 1
                
        
        # code here



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        n=int(input())
        arr=[int(x) for x in input().strip().split()]
        ob=Solution()
        ob.sort012(arr,n)
        for i in arr:
            print(i, end=' ')
        print()

# } Driver Code Ends