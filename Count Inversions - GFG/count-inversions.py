class Solution:
    # Function to count inversions in the array.
    def inversionCount(self, arr, n):
        # Helper function to perform merge sort and count inversions
        def merge_sort(arr, temp, left, right):
            inv_count = 0
            if left < right:
                mid = (left + right) // 2

                # Recursive call on the left and right halves
                inv_count += merge_sort(arr, temp, left, mid)
                inv_count += merge_sort(arr, temp, mid + 1, right)

                # Merge the sorted halves and count inversions
                inv_count += merge(arr, temp, left, mid, right)

            return inv_count

        # Helper function to merge two sorted halves and count inversions
        def merge(arr, temp, left, mid, right):
            i = left
            j = mid + 1
            k = left
            inv_count = 0

            while i <= mid and j <= right:
                if arr[i] <= arr[j]:
                    temp[k] = arr[i]
                    k += 1
                    i += 1
                else:
                    # If arr[i] > arr[j], it forms inversions with all elements in the left subarray
                    temp[k] = arr[j]
                    k += 1
                    j += 1
                    inv_count += mid - i + 1

            # Copy the remaining elements from both halves
            while i <= mid:
                temp[k] = arr[i]
                k += 1
                i += 1
            while j <= right:
                temp[k] = arr[j]
                k += 1
                j += 1

            # Copy the merged elements back to the original array
            for i in range(left, right + 1):
                arr[i] = temp[i]

            return inv_count

        # Create a temporary array to store merged results
        temp = [0] * n

        # Call the merge_sort function
        result = merge_sort(arr, temp, 0, n - 1)

        return result

# Driver Code



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
    for tt in range(t):
        n = int(input())
        a = list(map(int, input().strip().split()))
        obj = Solution()
        print(obj.inversionCount(a,n))
# } Driver Code Ends