import random, copy
import numpy as np

def InitIsite(SiteNum, SitePerson):
    '''
    初始化
    :param SiteNum: 座位数
    :param SitePerson: 已坐人数
    :return: 初始化座位， 已坐座位
    '''
    global InitSite
    InitSite = [i for i in range(1, SiteNum + 1)]  # 座位是数组的结构
    cc = lambda x: exec("InitSite[x] = 0")
    HaveSite = random.sample(InitSite, SitePerson)
    [cc(x - 1) for x in HaveSite]
    print("初始化的座位： {},  0为已坐".format(InitSite))
    return InitSite, HaveSite

def ReturnSite(site):
    '''
    不考虑最近距离为1
    获取所有可坐的位置
    '''
    ResultList = []
    recent = []
    num = 0
    site = site+[0]
    Cp_size = copy.copy(site)
    while Cp_size:
        if site[num]:
            recent.append(site[num])
        elif not site[num] and recent:
            if recent[0] == site[0]:
                if len(recent) >= 2:
                    ResultList.extend(recent[:-1])
            elif recent[-1] == site[-2]:
                if len(recent) >= 2:
                    ResultList.extend(recent)
            else:
                if len(recent) >= 3:
                    ResultList.extend(recent[1:-1])
            recent = []
        num += 1
        Cp_size = Cp_size[1:]
    if not ResultList:
        print("不存在远离所有人的位置")
        return None
    return ResultList

def CalSite(CanSite, HaveSite):
    '''
    处理座位与其他人最远距离
    CanSite：可坐的位置
    HaveSite：已坐的位置
    Return: SumList
    '''
    MA = np.mat([[i for x in range(len(HaveSite))]for i in CanSite])
    MB = np.mat([[x for x in HaveSite]for i in range(len(CanSite))])
    Disten = abs(MA - MB)
    SumDisten = np.sum(Disten, axis=1)
    MaxDisten = SumDisten.T.tolist()[0]
    return MaxDisten


def MainSite(SiteNum, SitePerson):
    ''' main '''
    Init = InitIsite(SiteNum, SitePerson)
    site = Init[0]
    HaveSite = Init[-1]
    HaveSite.sort()
    CanSite = ReturnSite(site)
    if not CanSite:
        return
    print('可坐位置有：{}'.format(str(CanSite)[1:-1]))
    Result = CalSite(CanSite=CanSite,
                     HaveSite=HaveSite)
    if Result:
        MaxNum = max(Result)
        print('离所有人最远的位置是: {}'.format(','.join([str(CanSite[i]) for i in [x for x, y in enumerate(Result) if y == MaxNum]])))

if __name__ == '__main__':
    while True:
        SiteNum = int(input('座位一共有:'))
        SitePerson = int(input('已坐人数一共有:'))
        MainSite(SiteNum=SiteNum,
                 SitePerson=SitePerson)
