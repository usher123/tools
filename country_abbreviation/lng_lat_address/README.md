# 说明
通过gcj02坐标系来进行定位，支持输入百度坐标系

定位思路：
- 将输入的经纬坐标转换成距离，通过二分查找筛选出最相近的N个坐标点
- 再将输入的经纬坐标与筛选出的坐标进行余弦相似处理
- 设置0.999999为阈值，做最后的筛选
- [——————————](#test)



---
## test