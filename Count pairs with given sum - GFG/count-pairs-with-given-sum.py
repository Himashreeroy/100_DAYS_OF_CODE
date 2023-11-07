#User function Template for python3

class Solution:
    def getPairsCount(self, arr, n, k):
        # code here
        count = 0
        num_dict = {}

        for num in arr:
            complement = k - num

            if complement in num_dict:
                count += num_dict[complement]

            if num in num_dict:
                num_dict[num] += 1
            else:
                num_dict[num] = 1

        return count
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n, k = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.getPairsCount(arr, n, k)
        print(ans)
        tc -= 1

# } Driver Code Ends