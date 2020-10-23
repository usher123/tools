def Place(func_):
    '''print('{}, {}'.format(*Place()))'''
    citylist = list(open('citycook.txt', 'r', encoding='utf-8').read().split('\n'))
    citydict = {i[:i.find('\t')]: int(i[i.rfind('\t'):]) for i in citylist}
    city, weight = zip(*list(citydict.items()))
    sum_weight = 0
    sum_weight_list = []
    for num in weight:
        sum_weight += num
        sum_weight_list.append(sum_weight)
    Sum_ = sum(weight)
    def pull():
        func_()
        return city[bisect.bisect_right(sum_weight_list, random.randint(0, Sum_-1))]
    return pull
    
@Place
def Place_():
    return
    
if __name__ == '__main__':
    for i in range(10):
        print(Place_())
