#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2020/10/31 11:21
# @Author : lantianyun l30001819
# @File : parsesite.py




def parsesite(site):
    if site is None or site.strip()=="":
        return 'unknown'
    else:
        return site.lower()


print(parsesite(None))