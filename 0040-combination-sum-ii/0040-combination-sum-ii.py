from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(start, target, path, result):
            if target == 0:
                result.append(path)
                return
            for i in range(start, len(candidates)):
                # Skip duplicates to avoid duplicate combinations
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                # Skip if the current candidate is larger than the remaining target
                if candidates[i] > target:
                    continue
                # Use candidates[i] in the current combination
                backtrack(i + 1, target - candidates[i], path + [candidates[i]], result)
        
        result = []
        # Sort candidates to efficiently handle duplicates
        candidates.sort()
        # Start backtracking from the first candidate
        backtrack(0, target, [], result)
        return result

# Example usage
sol = Solution()
candidates1, target1 = [10, 1, 2, 7, 6, 1, 5], 8
candidates2, target2 = [2, 5, 2, 1, 2], 5

print(sol.combinationSum2(candidates1, target1))  # Output: [[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]]
print(sol.combinationSum2(candidates2, target2))  # Output: [[1, 2, 2], [5]]
