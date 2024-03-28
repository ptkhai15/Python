Dict_1 = {'zero':0, 'one':1, 'two':2, 'three':3, 'four':4, 'five': 5}
type(Dict_1) //dict
Dict_2 = {'zero':0, 'one':1, 'two':2, 'three':3, 'four':4, 'four':5}
print(Dict_2["four"])
Dict_["six"] = 6
Dict_1 //{'zero':0, 'one':1, 'two':2, 'three':3, 'four':4, 'five': 5, 'six':6}
del Dict_1["six"]
Dict_1 //{'zero':0, 'one':1, 'two':2, 'three':3, 'four':4, 'five': 5}
Dict_1C = Dict_1.copy()
Dict_1C.clear() //{}
Dict_1.items()
Dict_1.keys()
Dict_1.value()
Dict_12 = {"six":6,"seven":7,"eight":8}
Dict_1.update(Dict_12)

