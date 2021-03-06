def Time():
    _MAPPING = (u'零', u'一', u'二', u'三', u'四', u'五', u'六', u'七', u'八', u'九', u'十',
            u'十一', u'十二', u'十三', u'十四', u'十五', u'十六', u'十七', u'十八', u'十九')
    _P0 = (u'', u'十', u'百', u'千',)
    _S4 = 10 ** 2
    random_open = [True, False, False]
    next_open = [True, False]
    def month_day_(num):
        assert (0 <= num and num < _S4)
        if num < 20:
            return _MAPPING[num]
        else:
            lst = []
            while num >= 10:
                lst.append(num % 10)
                num = num / 10
            lst.append(num)
            c = len(lst)  # 位数
            result = u''
            for idx, val in enumerate(lst):
                val = int(val)
                if val != 0:
                    result += _P0[idx] + _MAPPING[val]
                    if idx < c - 1 and lst[idx + 1] == 0:
                        result += u'零'
            return result[::-1]

    def year_(num):
        num = str(num)
        num_dict = {"0": u"零", "1": u"一", "2": u"二",
                    "3": u"三", "4": u"四", "5": u"五",
                    "6": u"六", "7": u"七", "8": u"八",
                    "9": u"九"}
        listnum = list(num)
        shu = []
        for i in listnum:
            shu.append(num_dict[i])
        new_str = "".join(shu)
        return new_str

    current_day = ''
    current_year = random.randrange(1999, 2022, 1) if random.choice(next_open) else ''
    current_month = random.randrange(1, 13, 1) if random.choice(next_open) else ''
    if current_month:
        current_day = random.randrange(1, 30, 1) if random.choice(next_open) else ''
        if current_day:
            if random.choice(random_open):
                current_day = str(month_day_(current_day))+'日'
                random_open.append(True)
            else:
                current_day = str(current_day) + "日"
                random_open.append(False)
    else:
        if not current_year:
            return random.choice(['昨天', '大前天', '前天', '上周', '上个月', '前几周', '前几个月'])

    if current_year:
        if random.choice(random_open):
            current_year = str(year_(current_year)) + '年'
            random_open.append(True)
        elif not current_month and random.choice(next_open):
            return random.choice(['今年', '去年', '前年', '大前年', '前几年', '十年前'])
        else:
            current_year = str(current_year) + '年'
            random_open.append(False)

    if current_month:
        if random.choice(random_open):
            current_month = str(month_day_(current_month)) + '月'
        else:
            current_month = str(current_month) + '月'
    return ''.join([current_year, current_month, current_day])
