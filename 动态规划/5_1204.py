#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2020/12/4 14:07
# @Author : lantianyun l30001819
# @File : 5_1204.py


# 最长回文子串
# "abbdss"  最长ab  输出ab


# 1.暴力法，以某个字符为中心，向两边扩散
class Solution1(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        len_ = len(s)
        max_sub = ""
        max_sub_len = 0
        for index, char in enumerate(s):

            i, j= index, index
            while i >= 0 and j <= len_ - 1 and s[i] == s[j]:
                i -= 1
                j += 1
            len_ji = j - i + 1
            max_sub_ji = s[i + 1:j]

            i, j = index, index+1
            while i >= 0 and j <= len_ - 1 and s[i] == s[j]:
                i -= 1
                j += 1
            len_ou = j - i + 1
            max_sub_ou = s[i + 1:j]



            if len_ji >= len_ou and len_ji > max_sub_len:
                max_sub_len = len_ji
                max_sub = max_sub_ji
            elif len_ou >= len_ji and len_ou > max_sub_len:
                max_sub_len = len_ou
                max_sub = max_sub_ou
        return max_sub


s = Solution1()
print(s.longestPalindrome("busislnescsicxpvvysuqgcudefrfjbwwjcchtgqyajdfwvkypfwshnihjdztgmyuuljxgvhdiwphrweyfkbnjgerkmifbirubhseuhrugwrabnjafnbdfjnufdstjbkuwtnpflffaqmjbhssjlnqftgjiglvvequhapasarlkcvbmkwnkuvwktbgfoaxteprobdwswcdyddyvrehvmxrrjiiidatidlpihkbmmruysmhhsncmfdanafdrfpdtfgkglcqpwrrtvacuicohspkounojuziittugpqjyhhkwfnflozbispehrtrnizowrlzcuollagxwtznjwzcumvedjwokueuqktvvouwnsmpxqvvpuwprezrbobrpnwaccwljchdguubjulyilzvmandjjleitweybqkjttschrjjlebnmponvlktzzcdtuybugggcqffkcffpamauvxfbonjrobgpvlyzveiwemmtdvbjciaytvesnocnjrwodtcokgcuoiicxapmrzpkfphjniuvzjrhbnqndfshoduejyktebgdabidxlkstepuwvtrtgbxaeheylicvhrxddijshcvdadxzsccmainyfpfdhqdanfccqkzlmhsfilvoybqojlvbcixjzqpbngdvesuokbxhkomsiqfyukvspqthlzxdnlwthrgaxhtpjzhrugqbfokrdcyurivmzgtynoqfjbafboselxnfupnpqlryvlcxeksirvufepfwczosrrjpudbwqxwldgjyfjhzlzcojxyqjyxxiqvfhjdwtgoqbyeocffnyxhyyiqspnvrpxmrtcnviukrjvpavervvztoxajriuvxqveqsrttjqepvvahywuzwtmgyrzduxfqspeipimyoxmkadrvrdyefekjxcmsmzmtbugyckcbjsrymszftjyllfmoeoylzeahnrxlxpnlvlvzltwnmldi"))
