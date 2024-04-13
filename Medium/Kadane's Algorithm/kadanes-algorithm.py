#User function Template for python3

class Solution:
    ##Complete this function
    #Function to find the sum of contiguous subarray with maximum sum.
    def maxSubArraySum(self,arr,N):
        ##Your code here
        
        global_maxi = arr[0]
        local_maxi = arr[0]
        sum = 0
        for i in range(1,N):
            local_maxi = max(arr[i],local_maxi+arr[i])
            global_maxi = max(local_maxi,global_maxi)
        return global_maxi
            
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math

 
def main():
        T=int(input())
        while(T>0):
            
            n=int(input())
            
            arr=[int(x) for x in input().strip().split()]
            
            ob=Solution()
            
            print(ob.maxSubArraySum(arr,n))
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends