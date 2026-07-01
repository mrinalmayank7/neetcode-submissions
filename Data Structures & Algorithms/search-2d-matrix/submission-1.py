class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        low = 0
        m=len(matrix)
        n= len(matrix[0])
        high = m*n -1
        
        print(high)
        while low <=high:
            mid = (low + high)//2
            # convert mid to 2D position
            row = mid // n    # which row
            col = mid % n     # which column

            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                low = mid + 1
            else:
                high = mid -1

        return False   