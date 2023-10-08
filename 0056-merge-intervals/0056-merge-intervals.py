class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        
        # Sort intervals based on the start time
        intervals.sort(key=lambda x: x[0])
        
        merged_intervals = [intervals[0]]
        
        for interval in intervals[1:]:
            # If the current interval overlaps with the last merged interval, merge them
            if interval[0] <= merged_intervals[-1][1]:
                merged_intervals[-1][1] = max(merged_intervals[-1][1], interval[1])
            else:
                # If there is no overlap, add the current interval to the merged intervals
                merged_intervals.append(interval)
        
        return merged_intervals
