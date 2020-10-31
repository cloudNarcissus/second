#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2020/10/31 14:54
# @Author : lantianyun l30001819
# @File : 406_reconstructQueue.py


#每个人由一个整数对(h, k)表示，其中h是这个人的身高，k是排在这个人前面且身高大于或等于h的人数。 编写一个算法来重建这个队列。

# 输入
people = [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]

# 首先按照h从大大小排序，然后按照k从小到大排序得到：
# [[7,0], [7,1], [6,1],[5,0], [5,2], [4,4]] 发现，先排最高的7，则k是不会变的，因为比7矮的无论放在哪里都不影响k的值。
# 因此思路就是把后面的元素一个个往前插

from typing import List

class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        # 注意双重排序，先按优先级低的，再按优先级高的排
        people.sort(key=lambda x: x[1])
        people.sort(key=lambda x:x[0],reverse=True)

        # 然后定义结果list，一个个插入：
        res = []
        for h,k in people:
            if res:
                exist_h = res[-1][0] #已排好的队列中最后一个的h
                if exist_h == h:
                    res.append([h, k])
                else: # 一定更小
                    res.insert(k,[h,k])
            else:
                res.append([h,k])

        return res


s = Solution()
print(s.reconstructQueue(people))





