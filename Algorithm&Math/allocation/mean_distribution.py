import random
import math

def meanDistr(sun, pe):
    """
    均值分配, 整体均值相差不大，更平滑
    sun 总分配额
    pe 分配个数
     """
    lk = []
    while pe > 1:
        avgp = math.floor(sun / pe)
        while 1:
            hg = avgp + random.randrange(1, avgp) * (-1 if pe % 2 else 1)
            if sun - hg != 0:
                break
        lk.append(hg)
        sun -= hg
        pe -= 1
    lk.append(sun)
    lk.sort(reverse=True)
    return lk