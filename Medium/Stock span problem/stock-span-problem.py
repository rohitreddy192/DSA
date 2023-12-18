#User function Template for python3


class Solution:
    
    #Function to calculate the span of stockâ€™s price for all n days.
    def calculateSpan(self,prices,n):
        stack = []  # to store indices
        span = [0] * n  # to store spans
        
        for i in range(n):
            # Pop elements from the stack while the current price is greater than prices[stack[-1]]
            while stack and prices[i] >= prices[stack[-1]]:
                stack.pop()
            
            # If the stack is empty, then the current day's price has been the greatest so far
            if not stack:
                span[i] = i + 1
            else:
                # Calculate the span by finding the difference between the current day and the index at the top of the stack
                span[i] = i - stack[-1]
            
            # Push the current index onto the stack
            stack.append(i)
        
        return span


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

#Contributed by : Nikhil Kumar Singh

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n = int(input())
        a = list(map(int,input().strip().split()))
        obj = Solution()
        ans = obj.calculateSpan(a, n);
        for i in range(n):
            print(ans[i],end=" ")
        print()            
# } Driver Code Ends