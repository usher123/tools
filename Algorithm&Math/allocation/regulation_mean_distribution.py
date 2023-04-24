import random
import math

def regMeanDistr(sun, pe, reg=4):
    """
    优先分配前面, 通过reg限制每份资源分配上限
    sun 总分配额
    pe 分配个数
     """
    lk = []
    while pe > 1:
        if sun == pe:
            lk.append(1)
        else:
            max_ = int((sun - pe) / reg) if sun - pe > reg else reg
            xj = random.randrange(1, max_) if max_!=1 else max_
            lk.append(xj)
            sun -= xj
        pe -= 1
    lk.append(sun)
    lk.sort(reverse=True)
    return lk