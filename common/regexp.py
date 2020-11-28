#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2020/11/24 17:25
# @Author : lantianyun l30001819
# @File : regexp.py



import re

text = "abc123abdsab12ddd3ab"
pat = re.compile(r'(?P<nima>ab.*?ab).*(ab.*?ab)')
x = pat.match(text)
print(x)
print(re.match(pat, text).group('nima'))