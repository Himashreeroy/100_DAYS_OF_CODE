#User function Template for python3


class Solution:
    def missingNumber(self,array,n):
        # code here
        expected_sum = (n * (n + 1)) // 2  # Sum of numbers from 1 to N
        actual_sum = sum(array)  # Sum of elements in the array
        missing_number = expected_sum - actual_sum
        return missing_number



#{ 
 # Driver Code Starts
#Initial Template for Python 3




t=int(input())
for _ in range(0,t):
    n=int(input())
    a=list(map(int,input().split()))
    s=Solution().missingNumber(a,n)
    print(s)
# } Driver Code Ends