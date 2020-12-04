#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2020/11/16 15:32
# @Author : lantianyun l30001819
# @File : ordereddict.py


from collections import OrderedDict
d1 = OrderedDict()
d1['b'] = 'B'
d1['a'] = 'A'
d1['c'] = 'C'
d1['1'] = '1'
d1['2'] = '2'

for k, v in d1.items():
    print(k, v)



dict1 = {1: 2, 2: 2, 3: 1, 4: 7, 5: 6, 6: 4, 7: 3, 8: 2, 9: 1}
d1 = sorted(dict1.values(), reverse=True)  # 按values值进行排序
d2 = sorted(dict1)
d3 = sorted(dict1.keys(), reverse=True)  # 按key值进行排序
print(d1)
print(d2)
print(d3)



from itertools import permutations
n = 4
k = 25
a = [str(i) for i in range(1, n+1)]
it = permutations(a, n)
for i in range(len(it)):
    print(next(it))


dict1 = {1: 2, 2: 2, 3: 1, 4: 7, 5: 6, 6: 4, 7: 3, 8: 2, 9: 1}
for k,v in enumerate(dict1.items()):
    print(k,v)