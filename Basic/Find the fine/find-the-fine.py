#User function Template for python3

class Solution:
    def totalFine(self, n, date, car, fine):
        odd = date%2 == 0 
        sum = 0
        for i in range(n):
            if odd and car[i]%2==1:
                sum += fine[i]
            elif not odd and car[i]%2==0:
                sum += fine[i]
        return sum
            
        #Code here
    
    
    


#{ 
 # Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n, k = [int(x) for x in input().strip().split()]
        arr = [int(x) for x in input().strip().split()]
        brr = [int(x) for x in input().strip().split()]
        
        print(Solution().totalFine( n, k, arr, brr))

        T -= 1


if __name__ == "__main__":
    main()


# } Driver Code Ends