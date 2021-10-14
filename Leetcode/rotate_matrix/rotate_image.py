"""
任意角度的旋转，会改变原始图片的整体大小，需要扩展原始矩阵。
"""
import cv2
from typing import List
from math import *

class ImageBox:
    """
    图片信息记录类
    """
    def __init__(self, imagepath: str, color=1) -> None:
        self.matrixImage(imagepath, color)
        
    def newHeight(self, height: int) -> None:
        """
        图片长度
        """
        self.height = height
        
    def newWidth(self, width: int) -> None:
        """
        图片宽度
        """
        self.width = width
    
    def shapeImage(self, imageShape: List[List[int or List[int]]]) -> None:
        """
        图像形状信息
        """
        self.left, self.top, self.right, self.bottom= imageShape
    
    def matrixImage(self, imagepath: str, color=1) -> None:
        """
        图像矩阵
        """
        self.IMG = cv2.imread(imagepath, color)
        self.shapeImage([0, 0, self.IMG.shape[1], self.IMG.shape[0]])
        
        
class Rotate:
    """
    图像处理类
    """
    def rotation(self,ImageBox: object, startangle: int, degree=45) -> None:
        """
        旋转
        """
        heightNew=int(ImageBox.right * fabs(sin(radians(degree))) + ImageBox.bottom * fabs(cos(radians(degree))))  # 扩长
        widthNew=int(ImageBox.bottom * fabs(sin(radians(degree))) + ImageBox.right * fabs(cos(radians(degree))))  # 扩宽
        ImageBox.newHeight(heightNew)
        ImageBox.newWidth(widthNew)
        
        center = ((ImageBox.left + ImageBox.right) / 2, (ImageBox.top + ImageBox.bottom) / 2)  # 中心点
        rot_mat = cv2.getRotationMatrix2D(center, startangle, 1)  # 中心点旋转
        rot_mat[0,2] += (widthNew-ImageBox.right)/ 2   
        rot_mat[1,2] += (heightNew-ImageBox.bottom)/ 2
        rotatedImg = cv2.warpAffine(ImageBox.IMG,  # 输入图像 
                                    rot_mat, # 变换矩阵
                                    (widthNew, heightNew),  # 输出图像大小
                                    borderMode=cv2.BORDER_CONSTANT,  # 边界像素模式
                                    borderValue=(255,255,255))  # 边界填充值
        return rotatedImg
      
if __name__ == "__main__":
  imagepath = 'xxxxx'
  angle = 45
  rotatedImage = Rotate().rotation(ImageBox(imagepath), startangle=angle)

