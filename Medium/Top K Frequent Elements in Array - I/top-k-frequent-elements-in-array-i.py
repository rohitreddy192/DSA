class Solution:
    def topK(self, nums, k):
        d = dict()
        for i in nums:
            d[i] = d.get(i,0) + 1
        l = sorted(d.items(),reverse = True, key = lambda x: [x[1],x[0]])[:k]
        return [l[i][0] for i in range(k)] 
        
            
        #Code here





#{ 
 # Driver Code Starts
		
if __name__ == '__main__':
    T=int(input())
    for i in range(T):
    	a = list(map(int, input().strip().split()))
    	n = a[0]
    	nums = a[1:]
    	k = int(input().strip())
    	obj = Solution()
    	ans = obj.topK(nums, k)
    	for i in ans:
    		print(i, end = " ")
    	print()
    	
# } Driver Code Ends