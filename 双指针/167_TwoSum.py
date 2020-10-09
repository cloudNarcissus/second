#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2020/10/9 16:15
# @Author : lantianyun l30001819
# @File : 167_TwoSum.py


# 两数和

from typing import List

class Solution:
    @classmethod
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        if len(numbers)<=1:
            return None

        head = 0
        tail = len(numbers)-1

        while head<tail:
            if numbers[head] + numbers[tail] == target:
                return [head+1,tail+1]
            elif numbers[head] + numbers[tail] > target:
                tail = tail - 1
            elif numbers[head] + numbers[tail] < target:
                head = head + 1
        else:
            return None


numbers=[2, 7, 11, 15]
target = 9
print(Solution.twoSum(numbers,target))