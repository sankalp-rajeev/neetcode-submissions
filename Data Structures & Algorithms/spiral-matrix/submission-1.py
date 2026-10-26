class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
    
        result = []
        while matrix:
            # 1 top-row
            result+=matrix.pop(0)

            row = len(matrix)
            # 2 going down:
            if matrix and matrix[0]: 
                for i in range(row):
                    result.append(matrix[i].pop())
                matrix = [row for row in matrix if row]
            if matrix and matrix[0]:
                # 3 going left
                n = len(matrix[-1])
                for i in range(n):
                    result.append(matrix[-1].pop())
                matrix.pop()
            if matrix and matrix[0]: 
                # 4 going up
                for i in range(len(matrix)-1,-1,-1):
                    result.append(matrix[i].pop(0))
        return result

