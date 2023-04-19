"""
经纬度确定位置
LngLatMagic.init_address()

"""
import json
import math
import numpy as np
import os

def out_of_china(lng, lat):
    """
    判断是否在国内
    :param lng:
    :param lat:
    :return:
    """
    return not (73.66 < lng < 135.05 and 3.86 < lat < 53.55)


class LngLatMagic:
    area_json = {}
    long_d = {}
    lng_lat = {}
    x_y = {}
    xi = []

    @classmethod
    def init_address(cls):
        """ 初始化 """
        with open('.\\ch_geo.md',
                  encoding='UTF-8'
                  ) as f:
            cls.area_json = json.load(f)
            f.close()
        [i.update({'index': index}) for index, i in enumerate(cls.area_json)]

        for area in cls.area_json:
            key_ = f"{area.get('lng')}_{area.get('lat')}"
            if area.get('lat') and area.get('lng'):
                cls.lng_lat[area.get('lat')] = set(list(cls.lng_lat.pop(area.get('lat'), [])) + [area.get('lng')])
                cls.lng_lat[area.get('lng')] = set(list(cls.lng_lat.pop(area.get('lng'), [])) + [area.get('lat')])
                cls.x_y.update({key_: {'name': area.get('province') + area.get('city') + area.get('area'),
                                       'index': area.get('index'),
                                       'vector': math.sqrt(float(area.get('lng')) ** 2 + float(area.get('lat')) ** 2)}})

        for i in cls.x_y:
            data = cls.x_y.get(i)
            cls.long_d[str(data.get('vector'))] = set(
                list(cls.lng_lat.pop(data.get('vector'), [])) + [data.get('index')])

        cls.xi = [float(ji) for ji in cls.long_d.keys()]
        cls.xi.sort()

    @staticmethod
    def binary_search_near_floor(Lit: list, num: [float, str]):
        """ 二分查找 """
        num = float(num)
        max_ = len(Lit)
        min_ = 0
        recl = int(max_ / 2)

        while max_ - min_ > 1:
            if Lit[recl] > num:
                max_ = recl

            elif Lit[recl] < num:
                min_ = recl
            else:
                return Lit[recl], recl

            recl = int((int(max_) - min_) / 2) + min_
        return Lit[min_], min_

    @classmethod
    def distance_address(cls, vector):
        """ 距离选取 """
        floor_get = 5
        upper_get = 6
        address_floor, index_lng_ = cls.binary_search_near_floor(cls.xi, vector)
        return address_floor, index_lng_, cls.xi[(lambda x: x - floor_get
                                                  if x >= floor_get
                                                  else 0)(index_lng_):
                                                 (lambda x: x + upper_get
                                                 if x + upper_get <= len(cls.xi) - 1
                                                 else len(cls.xi) - 1)(index_lng_)]

    @staticmethod
    def get_cos_similar(v1, v2):
        """ 余弦相似 """
        num = float(np.dot(v1, v2))
        denom = np.linalg.norm(v1) * np.linalg.norm(v2)
        return 0.5 + 0.5 * (num / denom) if denom != 0 else 0

    @classmethod
    def lng_lat_to_address(cls, lng: float, lat: float, model="GCJ02") -> tuple:
        """ 经纬度查找城市 """
        if model == "BD09":
            lng, lat = ExLngLat.bd09_to_gcj02(bd_lng=lng,
                                              bd_lat=lat)

        _, _, distance_top = cls.distance_address(math.sqrt(lng ** 2 + lat ** 2))
        bk = set()
        [[bk.add(dd) for dd in cls.long_d.get(str(zz))] for zz in distance_top]
        newd = [dict(cls.area_json[index_],
                     **{'dinct': cls.get_cos_similar([lng, lat],
                                                     [float(cls.area_json[index_].get('lng')),
                                                      float(cls.area_json[index_].get('lat'))])})
                for index_ in bk]

        newd.sort(key=lambda x: x.get('dinct'))
        return ''.join([newd[-1]['province'],
                        (newd[-1]['city'] if newd[-1]['dinct'] >= 0.999999 else ''),
                        (newd[-1]['area'] if newd[-1]['dinct'] >= 0.9999995 else '')]) \
                   if newd[-1]['dinct'] >= 0.99997 else None, newd[-1]


LngLatMagic.init_address()


class ExLngLat:
    x_pi = 3.14159265358979324 * 3000.0 / 180.0
    pi = 3.1415926535897932384626  # π

    @classmethod
    def bd09_to_gcj02(cls, bd_lng, bd_lat):
        """
        百度坐标系(BD-09)转火星坐标系(GCJ-02)
        百度——>谷歌、高德
        :param bd_lat:百度坐标纬度
        :param bd_lon:百度坐标经度
        :return:转换后的坐标列表形式
        """
        x = bd_lng - 0.0065
        y = bd_lat - 0.006
        z = math.sqrt(x * x + y * y) - 0.00002 * math.sin(y * cls.x_pi)
        theta = math.atan2(y, x) - 0.000003 * math.cos(x * cls.x_pi)
        gg_lng = z * math.cos(theta)
        gg_lat = z * math.sin(theta)
        return [gg_lng, gg_lat]


