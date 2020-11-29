#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2020/11/28 9:13
# @Author : lantianyun l30001819
# @File : 3_lengthOfLongestSubstring.py

# 找出最长的不含重复字符的子串

# 输入: s = "abcabcbb"
# 输出: 3
# 解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。


# 方法一：暴力法。以每个字符开头的子串都计算一次最大长度

from collections import deque
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        q = deque()
        max_sub_len = 0
        for i in range(len(s)):
            q.clear()
            for j in range(i,len(s)):
                if s[j] not in q:
                    q.append(s[j])
                else:
                    break
            max_sub_len = max(max_sub_len, len(q))
        return max_sub_len


# 方法二，跟法一一样，只不过数据结构换为dict/set 这样判断if sl[j] not in q更快。
class Solution2:
    def lengthOfLongestSubstring(self, s: str) -> int:
        q = set()
        max_sub_len = 0
        for i in range(len(s)):
            q.clear()
            for j in range(i,len(s)) :
                if s[j] not in q:
                    q.add(s[j])
                else:
                    break
            max_sub_len = max(max_sub_len, len(q))
        return max_sub_len


# 方法三：滑动窗口。 上个方法中，每次右指针j都要从i开始重新扫描，其实不需要
class Solution3:
    def lengthOfLongestSubstring(self, s: str) -> int:
        q = set()
        n = len(s)
        # 右指针，初始值为0
        j, ans = 0, 0
        for i in range(n):
            if q:
                q.remove(s[i - 1])
            while j < n and s[j] not in q: # 跟方法二的区别就是，j不再重复遍历之前遍历过的字符
                q.add(s[j])
                j += 1

            # 第 i 到 rk 个字符是一个极长的无重复字符子串
            ans = max(ans, len(q))
        return ans


s3 = Solution3()
print(s3.lengthOfLongestSubstring("pwwkew"))