"""
任意角度的旋转，会改变原始图片的整体大小，需要扩展原始矩阵。
"""
import cv2
from typing import List
import math

class ImageBox:
    """
    图片信息记录类
    """
    def __init__(self, imagepath: str, color=1) -> None:
        self.matrixImage(imagepath, color)
        
    def newHeight(self, height: int) -> None:
        """
        变更图片长度
        """
        self.height = height
        
    def newWidth(self, width: int) -> None:
        """
        变更图片宽度
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
        self.height = self.IMG.shape[0]
        self.width = self.IMG.shape[1]
        self.shapeImage([0, 0, self.IMG.shape[1], self.IMG.shape[0]])
        
        
class Rotate:
    """
    图像处理类
    """
    @staticmethod
    def rotation(ImageBox: object, startangle: int, degree=45) -> List[List[int or List[int]]]:
        """
        ImageBox： 图片信息类
        startangle： 旋转角度
        degree： 扩展度数
        
        desc： 图片旋转
        """
        heightNew = int(ImageBox.right * math.fabs(math.sin(math.radians(degree))) + 
                        ImageBox.bottom * math.fabs(math.cos(math.radians(degree))))  # 扩长
        
        widthNew = int(ImageBox.bottom * math.fabs(math.sin(math.radians(degree))) + 
                       ImageBox.right * math.fabs(math.cos(math.radians(degree))))  # 扩宽
        
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
    
    @staticmethod
    def show(IMG: List[List[int or List[int]]]) -> None:
        """
        IMG: 图片矩阵
        
        desc： 图片展示
        """
        cv2.imshow("IMG", IMG)
        cv2.resizeWindow("IMG", 860, 1280)
        cv2.waitKey()
        cv2.destroyAllWindows()
    
    
    @staticmethod
    def savepic(filepath: str, IMG: List[List[int or List[int]]]) -> None:
        """
        desc：图片保存
        """
        cv2.imwrite(filepath, IMG)
    
    @staticmethod
    def rotation_mark_rectangle(ImageBox: object, mark: list, angle=int) -> list:
        """
        ImageBox：图片信息类 
        mark：标记数据 [xmin, ymin, xmax, ymax]
        
        desc： 处理矩形标记区域的旋转变换
        标记数据eg：
                <xmin> 230 </xmin>
                <ymin> 41  </ymin>
                <xmax> 294 </xmax>
                <ymax> 297 </ymax>
        """
        
        def rotation_(x, y, angle, M, N):
            """
            计算旋转后坐标
            """
            _x = (x - M * 0.5) * math.cos(math.pi / 180.0 * angle) - (y - N * 0.5) * math.sin(math.pi / 180.0 * angle) + 0.5 * M
            _y = (x - M * 0.5) * math.sin(math.pi / 180.0 * angle) + (y - 0.5 * N) * math.cos(math.pi / 180.0 * angle) + 0.5 * N
            return _x, _y
        
        def scale(args):
            """
            计算后进行顺序排列
            """
            newlist = list(map(lambda x:[int(max(x)), int(min(x))], zip(*(args))))
            return [newlist[0][-1], newlist[-1][-1], newlist[0][0], newlist[-1][0]]
        
        def exmark(ImageBox: object, mark) -> tuple:
            """
            图片扩展后，标记会变化
            """
            exw = int((ImageBox.width - ImageBox.right) / 2)
            exh = int((ImageBox.height - ImageBox.bottom) / 2)

            xmin, xmax = mark[0] + exw, mark[2] + exw
            ymin, ymax= mark[1] + exh, mark[3] + exh
            
            return xmin, ymin, xmax, ymax
            
        xmin, ymin, xmax, ymax = exmark(ImageBox, mark)
        result = scale(list(map(rotation_, *list(zip(*[[xmin, ymin, -angle, ImageBox.width, ImageBox.height], 
                                                        [xmin, ymax, -angle, ImageBox.width, ImageBox.height],
                                                        [xmax, ymin, -angle, ImageBox.width, ImageBox.height],
                                                        [xmax, ymax, -angle, ImageBox.width, ImageBox.height]])))))
        return result
    
    
    
    
if __name__ == "__main__":
    imagepath = 'xxxxx'  # image 路径
    imginfo = ImageBox(imagepath)
    angle = 125  # 处理角度
    mark = [382, 168, 486, 383]  # 标记坐标 [xmin, ymin, xmax, ymax]
    Rotate.show(imginfo.IMG)  # 显示原图
    
    img_rotated_by_alpha = Rotate.rotation(imginfo, startangle=angle)
    Rotate.show(img_rotated_by_alpha)  # 显示旋转图
    exmark = Rotate.rotation_mark_rectangle(imginfo, mark, angle)
    Rotate.show(img_rotated_by_alpha[exmark[1]: exmark[3], exmark[0]: exmark[2]])  # 显示标记区域
    

