# 题目
给定一个 n × n 的二维矩阵 matrix 表示一个图像。请你将图像顺时针旋转 90 度。
你必须在 原地 旋转图像，这意味着你需要直接修改输入的二维矩阵。请不要 使用另一个矩阵来旋转图像。

示例 1：
输入：matrix = [[1,2,3],
                [4,5,6],
                [7,8,9]]
输出：[[7,4,1],
      [8,5,2],
      [9,6,3]]

示例 2：
输入：matrix = [[5,1,9,11],
               [2,4,8,10],
               [13,3,6,7],
               [15,14,12,16]]
输出：[[15,13,2,5],
      [14,3,4,1],
      [12,6,8,9],
      [16,7,10,11]]
      
示例 3：
输入：matrix = [[1]]
输出：[[1]]

示例 4：
输入：matrix = [[1,2],
                [3,4]]
输出：[[3,1],
      [4,2]]

* 因为是方阵的旋转，可以通过置换和镜像的组合进行变换，最终实现情况：
执行用时：28 ms
内存消耗：15 MB

## 拓展一
上述题目应用到图片处理中，可看成M * M的灰度图片的90，180，270角度旋转变换，如果换成是M * N的含有RGB三色矩阵，再进行角度为n的旋转，该怎么处理？
* 代码实现在：rotate_image
* 实现主要使用了opencv

## 拓展二
基于拓展一，如果原图片已经对物体打标，进行旋转后，如何一起打标？
* 代码实现在：rotate_image
* 实现主要使用了opencv

## 效果
* 原图标记到旋转后：
<img src="https://github.com/usher123/tools/tree/master/Q/Leetcode/rotate_matrix/pic/1.png" height="460" width="500" align=left/>
<img src="https://github.com/usher123/tools/tree/master/Q/Leetcode/rotate_matrix/pic/3.png" height="678" width="678" align=right/>

## 问题
* 在非常规角度扩图后的矩形截图会包含其他物体进去， 后来发现先通过标记，直接旋转后在原图上是可以保留标记的 =。=， 突然觉得这个拓展二有点鸡肋了，当作学习吧，效果如下：
<img src="https://github.com/usher123/tools/tree/master/Q/Leetcode/rotate_matrix/pic/2.png" height="678" width="678" align=left/>
