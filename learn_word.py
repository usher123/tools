import re, math
from collections import Counter
from array_clustering import array_clustering
from math_function import tanh

with open("D:\\zp_magic_box\\work\\game_category\\cn_stopwords.txt", encoding='utf-8') as fr:
    stop_words = set([word.strip() for word in fr])  # 停顿词的读取
    fr.close()


def deal_main(word_input):
    word_list = clear_word(word_input)
    word_count_list = []
    word_title_list = []
    for i in word_list:
        # split_list = split_word(i) #拆词成字，组合新词
        split_list = split_word_2(i) #拆词成字，组合新词
        word_count_list += split_list[0] #含重复词list
        word_title_list += split_list[1] #不含重复词list

    two_dict = counter_list(word_count_list, word_title_list) #list-》dict {word:num}
    word_score_dict = {} #每个词的密集度 {word:num}

    g_word = kill_min_word(word_num_dict=dict(two_dict[0]))

    all_title_num = len(word_input) #输入字段总数
    all_word_num = sum(list(g_word.values())) #总词数量 含重复

    #g_word = two_dict[0]

    for word in g_word.keys(): #计算每个词的密集度
        word_num = two_dict[0][word]
        word_title_num = two_dict[1][word]

        word_score_dict[word] = math_score(word_num, all_word_num, word_title_num, all_title_num)

    score_word_dict = transform_dict(word_score_dict) #key values 对换

    count_finger = list(set(list(word_score_dict.values()))) #清除重复密集数
    count_finger.sort()
    score_list = array_clustering(count_finger) #分类
    # score_list.pop(0) #去除分数最低位
    for x in score_list:
        split_word_list = (','.join([',' .join(score_word_dict[str(i)]) for i in x])).split(',') #从每个类里的密集数找出对应的词 [word1,word2...]
        pop_list = merge_list_similar_word(word_list=split_word_list) #找出金字塔组合顶部词汇
        print(deal_stop_word(pop_list))


def deal_stop_word(word):
    # cc = lambda x: [i.strip() for i in word if i != ' ' and i not in stop_words]  # 去除空格和停顿词，并整合成list
    cc = lambda x: word  # 去除空格和停顿词，并整合成list
    return cc(word)  # list


def kill_min_word(word_num_dict=None, loop_num=1):
    '''
    去除数量最少的词
    '''
    if type(word_num_dict) != type({}):
        raise Exception('input must be dict')
    deal_list = list(set(list(word_num_dict.values())))
    min_num = 1
    # loop_num = int(len(word_num_dict)/20000)
    for i in range(loop_num):
        try:
            min_num = min(deal_list)
        except:
            return kill_min_word(word_num_dict=word_num_dict, loop_num=loop_num-1)
        deal_list.pop(deal_list.index(min_num))
    return_dict = {k: x for k, x in word_num_dict.items() if x > min_num}
    return return_dict


def clear_word(*args):
    '''
    正则清理符号
    结构['word1','word2'....]
    '''
    return_list = []
    for i in args[0]:
        # i = re.sub(r'\d+', '', i) #去除数字
        i = ''.join(re.findall(r'([\w.]+)?', i.lower())) #去除符号
        # i = re.sub('_', '', ''.join(re.findall('(.*)_', i))) if '_' in i else i #保留最后一个“_”之前的数据
        # i = re.sub('_', '', i)# "_"全保留
        i = re.findall('(.*?)_|(.*)', i)
        i = i[0][0] if i[0][0] else i[0][1]# "_"全不保留
        return_list.append(i)

    return return_list

def split_word_2(word, exp_cut_num=7, min_word_len=2):
    '''
    split_word 优化版本,可减少不必要的词汇分解
    :param word:  str_word
    :param exp_cut_num: 期望一个句子里得到的词汇数
    :param min_word_len: 最小词汇长度
    :return:
    '''
    import re
    num_letter = [x for x in re.findall(r'[a-zA-Z]*[\d.]+[日月年a-zA-Z]?', word) if re.findall('\D+', x)]  # 抽离英文+数字,日期
    char_letter = [x for x in re.findall(r'[a-zA-Z]+', word) if re.findall('\D+', x)]  # 抽离英文
    word = re.sub(r'[a-zA-Z]*[\d.]+[日月年a-zA-Z]?', '', word)  # 清除英文+数字,日期
    word = re.sub(r'[a-zA-Z]+', '', word)  # 清除英文
    len_word = len(word)
    return_list = []
    if (len_word / min_word_len) > exp_cut_num:
        profuse_num = len_word - (exp_cut_num * min_word_len)
        first_word = [word[:x] for x in range(min_word_len, profuse_num + min_word_len + 1, 1)]
        return_list += first_word
        for i in range(0+min_word_len, len_word, min_word_len):
            if (len_word - i)-profuse_num > 0:
                for w in range(min_word_len):
                    first_word = [word[i+w:i+x] for x in range(min_word_len, profuse_num + min_word_len + 1, 1) if len(word[i+w:i+x]) > 1]
                    return_list += first_word
            else:
                if profuse_num >= min_word_len:
                    end_word = []
                    new_word = word[-profuse_num:]
                    for i in range(profuse_num - min_word_len+1):
                        if profuse_num - i - min_word_len >1:
                            for x in range(1, profuse_num - i):
                                end_word.append(new_word[i:i+x+1])
                        else:
                            end_word.append(new_word[i:])
                    return_list += end_word
                    break

        return return_list + num_letter + char_letter, list(set(return_list + num_letter + char_letter))
    else:
        return split_word_2(word, exp_cut_num=exp_cut_num-1)

def split_word(word, ori_limit_num = 8, item_word = None):
    '''
    input: str
    deal: limit_num = 4   'abcdef' -> [ab,abc,abcd,
                                       bc,bcd,bcde,
                                       cd,cde,cdef,
                                       de,def,
                                       ef]
    output:([ab,...,ef]含重复， [ab,....,ef]不含重复)

    拆分一个句子到charater级，再进行组合。含重复突显词频， 不含重复突显含该词的字段数。
    ori_limit_num: 最大词汇长度
    item_word: 新增： 去除高频，交叉词汇
    '''
    if not item_word:
    #     # item_word = ('手游', '火影忍者', '火影忍者手游', '火影忍者疾风传', '风暴', '攻略', '下载', '疾风传', '究极忍者风暴', '游戏')
    #     item_word = ('手游', '英雄联盟', '英雄联盟手游', 'lol', '皮肤', '攻略', '下载', '游戏', '英雄', 'lol', '云顶之弈', '琵琶网', '活动', '地址', '怎么', '什么', '召唤')
    #     item_word = ('steam', '游戏')
    #     item_word = ('wow', '魔兽', '魔兽世界', '专区', '魔兽世界专区', '攻略')
        item_word = ()

    return_single_word_list = []
    # num_letter = [x for x in re.findall(r'[\d.]+[日月年a-zA-Z]', word) if re.findall('\D+', x)] #抽离英文,英文+数字,日期
    num_letter = [x for x in re.findall(r'[a-zA-Z]*[\d.]+[日月年a-zA-Z]?', word) if re.findall('\D+', x)] #抽离英文+数字,日期
    char_letter = [x for x in re.findall(r'[a-zA-Z]+', word) if re.findall('\D+', x)] #抽离英文

    word = re.sub(r'[a-zA-Z]*[\d.]+[日月年a-zA-Z]?', '', word)  #清除英文+数字,日期
    word = re.sub(r'[a-zA-Z]+', '', word)  #清除英文
    char_list = list(word)
    word_len = len(char_list)
    skip_num = -1

    for i in range(word_len):
        if i <= skip_num:
            continue
        skip_num = -1
        limit_num = ori_limit_num if word_len - i >= ori_limit_num else word_len - i
        for y in range(limit_num-1, 0, -1): #倒排，剔除高频词汇后在进行组合
            # if i+y > word_len:
            #     continue
            new_word = char_list[i] + ''.join(char_list[i+1:i+y+1])
            if new_word in item_word:  #去除高频构造词
                skip_num = i+y
                break
            return_single_word_list.append(new_word)
    add_list = [i for i in num_letter + char_letter if i not in item_word]
    return_single_word_list += add_list
    # return_single_word_list += char_letter

    # print(return_single_word_list)
    return return_single_word_list, list(set(return_single_word_list))


def math_score(word_num, all_word_num, word_title_num, all_title_num):
    '''
    计算词的密集度： （该词所在总词频率） * exp（出现该次的字段的频率）
    :param word_num: 该词总数
    :param all_word_num: 总词数
    :param word_title_num: 该次所在的字段的总数
    :param all_title_num: 所有字段总数
    :return: float
    '''

    molecule = float('%0.4f' % (word_num / all_word_num))
    # denominator = math.exp(float('%0.4f' % (word_title_num / all_title_num)))
    denominator = math.log(float('%0.4f' % (all_title_num / (word_title_num + 1))))
    # return float('%0.4f' % ((molecule / denominator) *1000))
    return float('%0.6f' % tanh(float('%0.6f' % ((molecule * denominator * 1000) ))))
    # return float('%0.4f' %  tanh(molecule *1000))


def counter_list(word_count_list, word_title_list):
    '''
    计算各词所占总数量和 字段数量
    :param word_count_list: 所有词集合 含重复
    :param word_title_list: 每个字段词集合 不含重复
    :return:{word：num}
    '''
    count_count_dict = Counter(word_count_list)
    word_title_list = Counter(word_title_list)

    return count_count_dict, word_title_list
    # for i in list(count_dict.keys()):
    #     del count_dict[i]

def transform_dict(word_score_dict):
    '''
    转换key 和values
    :param word_score_dict: {word: num}
    :return:{num:[word1,word2]}
    '''
    score_word_dict = {}
    for x, y in zip(word_score_dict.keys(), word_score_dict.values()):
        if str(y) in score_word_dict:
            score_word_dict[str(y)].append(x)
        else:
            score_word_dict[str(y)] = [x]
    return score_word_dict

def merge_list_similar_word(word_list=None):
    '''
    组合离散程度相差不多的词组
    :param word_list:[word1,word2,word3] --> 频繁词一般会被分为金字塔型[ab,abc,abcd,bcd,cd,bc]
    :return: 金字塔顶端字符[abcd,defg]
    '''
    if not word_list:
        test_a = ['魔兽世界9', '魔兽世界9.', '魔兽世界9.0', '兽世界9', '兽世界9.', '兽世界9.0', '世界9', '世界9.', '世界9.0', '界9', '界9.', '界9.0', '怎么', '攻略',
         'lo', 'lol', 'ol', '公布', '王者荣耀鲁', '王者荣耀鲁班', '者荣耀鲁', '者荣耀鲁班', '荣耀鲁', '荣耀鲁班', '耀鲁', '耀鲁班', '鲁班', '等级', '等级上', '等级上限',
         '级上', '级上限', '上限', '安其', '安其拉', '安其拉废', '安其拉废墟', '安其拉废墟三', '安其拉废墟三件', '安其拉废墟三件套', '其拉', '其拉废', '其拉废墟', '其拉废墟三',
         '其拉废墟三件', '其拉废墟三件套', '拉废', '拉废墟', '拉废墟三', '拉废墟三件', '拉废墟三件套', '废墟', '废墟三', '废墟三件', '废墟三件套', '墟三', '墟三件', '墟三件套',
         '三件', '三件套', '件套', '宇航', '宇航员', '航员', '新手', '王者', '王者荣', '王者荣耀', '者荣', '者荣耀', '荣耀']
        test_b = ['总决赛', '联盟最', '王者', '选手', 'rng', '打野', 'ig', '无限', '装备', '符文', '联盟新', '英雄联盟中', '个英雄', '冠军', '玩法', '上单', '网友', '联盟中', '一个', '第一', '介绍', '更新', '战队', '的英雄', 'lpl', '出装', '攻略', '玩家', '英雄联盟手游', '版本', '技能', '什么', '联盟手游', '游戏', '怎么', 's', '皮肤', 'lol']
        word_list = test_b
    pyramid_dict = {}
    for i in word_list:
        for q in range(1, math.floor(len(i)/2)+1):
            kk = [i[:-q], i[q:]]
            # kk = [i[:-1], i[1:]]
            for k in kk:
                if k not in pyramid_dict:
                    pyramid_dict[k] = [i]
                else:
                    pyramid_dict[k].append(i)
    pop_list = []
    for i in word_list:
        if i not in pyramid_dict:
            pop_list.append(i)
    return pop_list



if __name__ == '__main__':
    a = [
                '《魔兽世界》9.0等级上限是多少 新版本等级上限机制详解',
                '魔兽世界安其拉废墟三件套怎么获得_安其拉废墟三件套获取攻略',
                '魔兽世界:暴雪蓝贴意外透露进程!9.0前期开放时间或将提前!',
                'LOL狗熊重做技能数值公布:满级大招能让防御塔失效6秒',
                'LOL宇航员系列新皮肤公布:巴德、纳尔、波比宇航员皮肤预览',
                '王者荣耀:鲁班皮肤哪个好?土豪选星空,大神却只用免费换的TA',
                '王者荣耀:鲁班七号出装？',
                '联动《和平精英》《王者荣耀》的背后,是小米游戏对渠道升级思考',
                '魔兽世界9.0新手怎w9.0暗影国度新手入门攻略_3DM网游'
                # '魔兽世界9.0新手0暗影国度_3DM网游',
                # '魔兽世界9.0新手怎么玩.0暗影国度入门攻略_3DM网游',
                # '魔兽世界9.0暗影国度_3DM网游'
                  ]
    # merge_list_similar_word()
    import json
    # with open('d:\\test2.txt', 'r') as f:
    #     a = f.read()
    #     f.close()
    # a = a[1:-1].split(',')
    # a.pop(a.index(' '))
    deal_main(a)
    # merge_list_similar_word()
