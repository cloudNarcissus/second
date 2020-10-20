#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2020/10/19 16:22
# @Author : lantianyun l30001819
# @File : cal_time.py

import time

def cal_time(func):
    def wrapper(*args,**kwargs):
        t1 = time.time()
        result = func(*args,**kwargs)
        t2 = time.time()
        print("%s 运行: %s 秒"%(func.__name__,t2-t1))
        return result
    return wrapper