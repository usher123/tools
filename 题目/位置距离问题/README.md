# Demo

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

```
