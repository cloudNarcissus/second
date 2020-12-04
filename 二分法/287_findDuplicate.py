#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2020/12/3 15:22
# @Author : lantianyun l30001819
# @File : 287_findDuplicate.py

# 题目：找到重复的数字
# 条件和要求：
# 数组长度为n+1，数字在 1~n之间，因此必然有一个数字重复
# 不能更改原数组（假设数组是只读的）。
# 只能使用额外的 O(1) 的空间。
# 时间复杂度小于 O(n2) 。
# 数组中只有一个重复的数字，但它可能不止重复出现一次。


class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 数字在1到n，那么对这1到n二分，
        # 比如[1,3,4,2,2]一共五个数，那么数字就是1到4之间。
        # 于是对1到4进行二分，拿到中值2，然后扫描数组小于中值的就累加cnt，如果扫描完毕发现cnt小于中值，说明重复的值在大于中值的那一半。反之亦然。
        low = 1
        high = len(nums)-1

        while low < high:    # 注意循环的结束条件就是low = high。 所以此处不能写 low <= high 否则会造成死循环
            mid = (low + high)//2
            cnt = 0
            for num in nums:
                if num <= mid:
                    cnt += 1
            if cnt <= mid:
                low = mid + 1
            else:
                high = mid

        return high  # 这里返回low 或者 high都行，因为两者一样


s = Solution()
print(s.findDuplicate([3,1,2,3,3,4]))


