from typing import List
class Solution:
    angle = 90
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        if Solution.angle == 90:  # 顺时针旋转90 是先转置 再做左右镜像
            self.rightleftMatrix(self.Transpose(matrix))
        elif Solution.angle == 180:  # 顺时针旋转180 则是上下， 左右各做镜像
            self.updownMatrix(self.rightleftMatrix(matrix))
        elif Solution.angle == 270:  # 顺时针270度 则是先转置， 后做上下镜像
            self.updownMatrix(self.Transpose(matrix))
        else:
            matrix

    def Transpose(self, matrix: List[List[int]]) -> list:
        """
        转置
        """
        for i in range(len(matrix)):
            for x in range(i, len(matrix)):
                matrix[i][x], matrix[x][i] = matrix[x][i], matrix[i][x]    
        return matrix
        
    def updownMatrix(self, matrix: List[List[int]]) -> list:
        """
        上下镜像
        """
        for x,y in zip(range(int(len(matrix) / 2)), range(len(matrix)-1, int(len(matrix) / 2 - 0.5), -1)):
            matrix[x], matrix[y] = matrix[y], matrix[x]
        return matrix

    def rightleftMatrix(self, matrix: List[List[int]]) -> list:
        """
        左右镜像
        """
        for i in range(len(matrix)):
            for x,y in zip(range(int(len(matrix) / 2)), range(len(matrix)-1, int(len(matrix) / 2 - 0.5), -1)):
                matrix[i][x], matrix[i][y] = matrix[i][y], matrix[i][x]    
        return matrix
