# 题目
“一个芬兰人进了一个房间，房间有一排椅子，椅子上有一些人坐着，还剩一些空位，他要选择一个位子坐下，这个位子要尽可能远离已经坐着的人，请给出算法。请自行定义数据结构和输入输出。” 

# Demo  不考虑相邻有人

```
while True:
    SiteNum = int(input('座位一共有:'))
    SitePerson = int(input('已坐人数一共有:'))
    MainSite(SiteNum=SiteNum,
             SitePerson=SitePerson)


>>> 座位一共有:10
>>> 已坐人数一共有:4
>>> 初始化的座位： [1, 0, 3, 4, 5, 0, 7, 0, 0, 10],  0为已坐
>>> 可坐位置有：4
>>> 离所有人最远的位置是: 4


>>> 座位一共有:10
>>> 已坐人数一共有:8
>>> 初始化的座位： [0, 0, 0, 0, 0, 0, 7, 8, 0, 0],  0为已坐
>>> 不存在远离所有人的位置


>>> 座位一共有:10
>>> 已坐人数一共有:6
>>> 初始化的座位： [1, 2, 0, 0, 0, 0, 0, 0, 9, 10],  0为已坐
>>> 可坐位置有：1, 10
>>> 离所有人最远的位置是: 1,10
```
