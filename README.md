# tools
一些没事无聊想到以后可能也许未必但又必要的工具



Project     |  Fuction   |  Problem  | Progress
----         |   -----------     |   -----------   |   ----------- 
country_abbreviation        |   国家转换缩写     |      |
array_clustering           | 一维数组的聚类  |相比kmeans聚类，多维需要在每个维度上的聚类后，再合并（猜想），不同于kmeans，不需要分类个数的限制，缺点：精准分类需要多次迭代，迭代后的loss暂无计算.
learn_word                 | 基于TF-IDF算法和array_clustering进行同类型句段，提取高频词汇              | 只能处理已分好类的集合，分离出来的词汇，不同类别之间需要去除总交集，才能突显不同类之间的高频词汇，且无信息熵的确定会有多余前后缀的影响| 
cn_stopwords  |   中文停顿词汇表     |      |
site  |   面试题：“一个芬兰人进了一个房间，房间有一排椅子，椅子上有一些人坐着，还剩一些空位，他要选择一个位子坐下，这个位子要尽可能远离已经坐着的人，请给出算法。请自行定义数据结构和输入输出。”     |      |
randomdate  |   随机生成阿拉伯数字与中文混合型的日期，简单用于时间抽取的样本生成     |      |
RandomCity|   权重随机二分查找中国市级及以上地区名，权重顺序首都-省级-省会城市-市级     |      |
Leetcode|   记录Leetcode上一些有意思的代码编写     |      |
