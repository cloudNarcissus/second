#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2020/10/16 18:04
# @Author : lantianyun l30001819
# @File : csv_op.py

import csv
with open('1275442.csv','r',encoding='UTF-8') as csvIN:
   for row in csv.reader(csvIN, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL):
       print(row)

print("======分割线===============分割线================分割线===================分割线===================")

import csv
content = open("1275442.csv", "r",encoding='UTF-8').read().replace('\\"',chr(1))
with open("1275442.csv.new", "w",encoding='UTF-8') as g:
    g.write(content)
with open('1275442.csv.new','r',encoding='UTF-8') as csvIN:
   for row in csv.reader(csvIN, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL):
       print(row)
