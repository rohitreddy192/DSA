#User function Template for python3


class Solution:
    #Function to check if a string can be obtained by rotating
    #another string by exactly 2 places.
    def isRotated(self,s1,s2):
        n = len(s1)
        if n == 2:
            return s1 == s2
        
        for i in range(n):
            if s1[(i + 2) % n] == s2[i] or s1[(n + i - 2) % n] == s2[i]:
                continue
            else:
                return False
        
        return True

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        s=str(input())
        p=str(input())
        if(Solution().isRotated(s,p)):
            print(1)
        else:
            print(0)
# } Driver Code Ends