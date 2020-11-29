#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2020/11/24 14:26
# @Author : lantianyun l30001819
# @File : 5_longestPalindrome.py





# 00   01   02   03
# 10   11   12   13
# 20   21   22   23
# 30   31   32   33
# 考虑上面的矩阵，x表示子串的起始位置，y表示子串的结束位置。因此这个矩阵就是长度为4的字符串的所有起止位置的组合
# 其中因为起始必然小于等于结束，所以对角线下方的都是无效的。
# 每个位置存储这个起止位置的子串是否是回文：
# 初始化都为0.
# 0   0   0   0
# 0   0   0   0
# 0   0   0   0
# 0   0   0   0

# 考虑一个回文字符串，该串去掉首位两个字符也必然是一个回文字符串。因此一个子串为回文，再加上前后两个字符相等，即可以得到更长的回文串：
# 因此从对角线开始，每个元素的右上对角的元素就可以由左下角得到。遍历方向从左下往右上，因此外层循环是子串长度
# 比如对角线上子串长度就是1，然后再往右上一条线的子串长度就是2，一直到矩阵的右上顶点（0,3）为止，达到最大长度4


class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n == 0 :
            return ""
        dp = [[False for _ in range(n)] for _ in range(n)]
        res = ""

        for len_ in range(n):  # len_ 表示横纵坐标的差值
            tag = ()
            for j in range(len_,n):
                i = j - len_  # i是横坐标

                if len_ == 0: # 差值为0表示子串为单个字符，满足回文
                    dp[i][j] = True
                    tag = (i,j)
                elif len_ == 1 and s[i] == s[j]: # 差值为1表示子串为两个字符，如果相等则为回文
                    dp[i][j] = True
                    tag = (i,j)
                elif len_ > 1 and dp[i+1][j-1] and s[i] == s[j]: # 差值超过1以后，就可以用状态转移式了，根据其左下角的元素的值和收尾值判断
                    dp[i][j] = True
                    tag = (i,j)
                else:
                    pass

            # 每次遍历完如果tag 为True说明此长度有回文。
            if tag:
                res = s[tag[0]:tag[1]+1]


        return res



s = Solution()
s.longestPalindrome('1234')



