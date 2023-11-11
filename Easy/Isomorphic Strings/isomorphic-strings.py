#User function Template for python3

class Solution:
    
    #Function to check if two strings are isomorphic.
    def areIsomorphic(self,s1,s2):
        n1, n2 = len(s1), len(s2)
        if n1 != n2:
            return False
    
        mapping = {}  # store mapping of s1 to s2
        visited = {}  # for s2
    
        for i in range(n1):
            c1, c2 = s1[i], s2[i]
            if c1 not in mapping:
                # c1 seen for the first time
                if c2 not in visited:
                    # c2 also seen for the first time, map c1->c2 and mark c2 vis.
                    mapping[c1] = c2
                    visited[c2] = 1
                # c1 is seen for the first time, but c2 is already mapped somewhere.
                elif visited[c2] == 1:
                    return False
            # c1 already mapped, but not to c2
            elif mapping[c1] != c2:
                return False
    
        return True
#{ 
 # Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys
from collections import defaultdict

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
        ob = Solution()
        if(ob.areIsomorphic(s,p)):
            print(1)
        else:
            print(0)
# } Driver Code Ends