cars = {'BWM': 8.5, 'BENS': 8.3, 'AUDI': 7.9}
#获取字典中所有的key-value对，返回一个dict_items对象
ims = cars.items()
print(type(ims))
#将dict_items对象转换成列表
print(list(ims))
#访问第二个key-value对
print(list(ims)[1])
#获取字典中所有的key
key = cars.keys()
print(type(key))
#将dict——keys转换成列表
print(list(key))
#访问第二个key
print(list(key)[1])
#获取字典中所有的value，返还一个dict-value对象
vals = cars.values()
#将dict-values转换成列表
print(type(vals))
#访问第二个vals
print(list(vals)[1])
