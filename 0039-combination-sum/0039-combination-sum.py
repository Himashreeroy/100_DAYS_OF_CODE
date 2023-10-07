from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(start, target, path, result):
            if target == 0:
                result.append(path)
                return
            for i in range(start, len(candidates)):
                if candidates[i] > target:
                    continue
                # Use candidates[i] in the current combination
                backtrack(i, target - candidates[i], path + [candidates[i]], result)
        
        result = []
        # Start backtracking from the first candidate
        backtrack(0, target, [], result)
        return result

# Example usage
sol = Solution()
candidates1, target1 = [2, 3, 6, 7], 7
candidates2, target2 = [2, 3, 5], 8
candidates3, target3 = [2], 1

print(sol.combinationSum(candidates1, target1))  # Output: [[2, 2, 3], [7]]
print(sol.combinationSum(candidates2, target2))  # Output: [[2, 2, 2, 2], [2, 3, 3], [3, 5]]
print(sol.combinationSum(candidates3, target3))  # Output: []

        