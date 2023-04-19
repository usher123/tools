from LLfunction import *

def run(lng: float, lat: float, model:str = 'GCJ02') -> [str, None]:
    """
    model: 
    默认 GCJ02坐标系
    BD09 百度坐标系  
    """
    result, _ = LngLatMagic.lng_lat_to_address(lng, lat, model=model)
    print("最相近的结果: ", result)
    return result if result and _.get('dinct') >= 0.999999 else None


if __name__ == "__main__":
    lng = float(input("lng: "))
    lat = float(input("lat: "))
    print(run(lng=lng, lat=lat))