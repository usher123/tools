# tools
一些没事无聊想到以后可能也许未必但又必要的工具



Project     |  Fuction   |  Problem  | Progress
----         |   -----------     |   -----------   |   ----------- 
country_abbreviation        |   国家转换缩写     |      |
array_clustering           | 一维数组的聚类  |相比kmeans聚类，多维需要在每个维度上的聚类后，再合并（猜想），不同于kmeans，不需要分类个数的限制，缺点：精准分类需要多次迭代，迭代后的loss暂无计算.
learn_word                 | 基于TF-IDF算法和array_clustering进行同类型句段，提取高频词汇              | 只能处理已分好类的集合，分离出来的词汇，不同类别之间需要去除总交集，才能突显不同类之间的高频词汇| 
cn_stopwords  |   中文停顿词汇表     |      |

