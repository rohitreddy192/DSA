#User function Template for python3

class Solution:    
    #Function to find the minimum number of platforms required at the
    #railway station such that no train waits.
    def minimumPlatform(self,n,arr,dep):
        arr.sort()
        dep.sort()
        i, j, res, platNeeded = 1, 0, 1, 1
        while(i<n and j<n):
            if(arr[i]<=dep[j]):
                platNeeded += 1
                i += 1
            else:
                platNeeded -= 1
                j+=1
            if(platNeeded>res):
                res = platNeeded
        return res
        
        # code here





#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

#Contributed by : Nagendra Jha


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n = int(input())
        arrival = list(map(int, input().strip().split()))
        departure = list(map(int, input().strip().split()))
        ob=Solution()
        print(ob.minimumPlatform(n,arrival,departure))
# } Driver Code Ends