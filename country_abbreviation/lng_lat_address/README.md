# 说明
通过gcj02坐标系来进行定位，支持输入百度坐标系

定位思路：
- 将输入的经纬坐标转换成距离，通过二分查找筛选出最相近的N个坐标点
- 再将输入的经纬坐标与筛选出的坐标进行余弦相似处理
- 设置0.999999为阈值，做最后的筛选

---
## BD09 Demo
### 百度地图拾取器：http://api.map.baidu.com/lbsapi/getpoint/index.html
```python
>>> run(lng=116.372505, lat=39.91405, model='BD09')
>>> "北京市市辖区西城区"

>>> run(lng=116.757842, lat=36.561875, model='BD09')
>>> "山东省济南市长清区"

>>> run(lng=113.949308, lat=22.530365, model='BD09')
>>> "广东省深圳市南山区"
```