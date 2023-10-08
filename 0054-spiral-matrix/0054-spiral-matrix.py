class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        
        result = []
        row_start, row_end, col_start, col_end = 0, len(matrix) - 1, 0, len(matrix[0]) - 1
        
        while row_start <= row_end and col_start <= col_end:
            # Traverse right
            for i in range(col_start, col_end + 1):
                result.append(matrix[row_start][i])
            row_start += 1
            
            # Traverse down
            for i in range(row_start, row_end + 1):
                result.append(matrix[i][col_end])
            col_end -= 1
            
            # Traverse left if there is a valid row
            if row_start <= row_end:
                for i in range(col_end, col_start - 1, -1):
                    result.append(matrix[row_end][i])
                row_end -= 1
            
            # Traverse up if there is a valid column
            if col_start <= col_end:
                for i in range(row_end, row_start - 1, -1):
                    result.append(matrix[i][col_start])
                col_start += 1
        
        return result
