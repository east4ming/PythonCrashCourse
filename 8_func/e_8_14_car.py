"""Car Info.

将一辆汽车的信息储存在一个字典中.
总是接受制造商和型号, 还有关键字实参. (如颜色和选装配件)
打印返回的字典.
"""
def make_car(manu, model, **car_info):
    """车的字典, 包括制造商和星号, 及其他关键字."""
    car = {}
    car['manufacturer'] = manu
    car['model'] = model
    for k, v in car_info.items():
        car[k] = v
    return car
car = make_car('subaru', 'outback', color='blue', tow_package=True)
print(car)
