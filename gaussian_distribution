import math
from functools import reduce


def gaussianDistribution(maxn:int, pe:int) -> list:
    """
    maxn: 需要被分配数
    pe:   分配人数
    """
    pe = maxn if pe > maxn else pe
    u = 0
    o = sum([i **2 for i in range(1, pe + 1)]) / pe   # o ** 2
    w = math.exp(maxn % pe)

    gaussianNum = [((1 / (math.sqrt(2 * math.pi))) * math.exp(-((x - u) ** 2 / (2 * o)))) * w  for x in range(pe)]
    
    
#     softmax_denominator = sum([math.exp(zx) for zx in gaussianNum]) 

#     softmax_score_distribution = [round(maxn * (math.exp(x)) / softmax_denominator) for x in gaussianNum]
    
    gaussianNum_reduce = [i - max(gaussianNum) for i in gaussianNum]
    
    softmax_denominator = sum([math.exp(zx) for zx in gaussianNum_reduce])
    softmax_score_distribution = [round(maxn * (math.exp(x)) / softmax_denominator) for x in gaussianNum_reduce]
    
    return softmax_score_distribution

    
