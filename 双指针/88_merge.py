#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2020/10/14 19:15
# @Author : lantianyun l30001819
# @File : 88_merge.py

from typing import List
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = 0
        j = 0
        new_list = []
        while i<m and j<n:
            if nums1[i]<=nums2[j]:
                new_list.append(nums1[i])
                i = i+1
            elif nums1[i]>nums2[j]:
                new_list.append(nums2[j])
                j = j+1

        if i == m:
            new_list.extend(nums2[j:n]) #注意传入的nums1中包含了很多0
        if j == n:
            new_list.extend(nums1[i:m])

        nums1[:]=new_list