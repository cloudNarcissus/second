#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2021/1/12 19:29
# @Author : lantianyun l30001819
# @File : 16_19_pondSizes.py


# 输入：
# [
#   [0,2,1,0],
#   [0,1,0,1],
#   [1,1,0,1],
#   [0,1,0,1]
# ]
# 输出： [1,2,4]


from typing import List

class Solution:
    def __init__(self):
        self.i = 0
        self.res = []

    def pondSizes(self, land: List[List[int]]) -> List[int]:

        m = len(land)
        n = len(land[0])

        def dfs(x, y):
            if not 0<= x < m or not 0<= y < n or land[x][y] != 0:
                return

            self.i += 1
            land[x][y] = 1

            dfs(x+1,y)
            dfs(x-1, y)
            dfs(x, y + 1)
            dfs(x, y - 1)
            dfs(x +1, y + 1)
            dfs(x -1, y - 1)
            dfs(x - 1, y + 1)
            dfs(x + 1, y - 1)

        for i in range(m):
            for j in range(n):
                self.i = 0
                dfs(i, j)
                if self.i > 0:
                    self.res.append(self.i)

        self.res.sort()

        return self.res



land =[
  [0,2,1,0],
  [0,1,0,1],
  [1,1,0,1],
  [0,1,0,1]
]
s = Solution()
print(s.pondSizes(land))




l =["checkstyle","simian","findbugs","sourcemonitor","sharpcounter","pmd","cobertura","sai","sloccount","compile","pygenie","sonarqube","uadpguarding","codedex","cseccheck","llt","codecc","Package","catchcheck","hutaf","duplicatefile","devtestc","agitar","nsiq","jslint","blackduck","flexelint","binaryfile","virusscan","devtest","deveco","ansiblelint","codecount","tslint","govet","envtest","devtestlcov","gocyclo","devtestjava","newcct","codecover","opensrcscan","eslint","scalastyle","jacoco","jshint","download","codecheck","codedexweb","buildmc","pylint","archguarding3","golint","androidlint","GoCover","jshint","CodeMars","sqlscan","CodeAnalyzer","Anystandard","Xmllint","Vlint","Vdiff","testBench","cmetrics","Canux","phoenixCA","pclint","phoenixlint","Xmllintlinux","gotest","codingstylecheck","devtestcGate","devtestlcovGate","buildmcenvcheck","compileOptionCheck","PythonTestcase","PylintScan","testcaseSpecification","jacoco","lltcov","pclintplus","lltcheck","sqlScan_CBGIT","strcheck","sqlScanCBGIT","gocycle","buildcheckDC","SecurityScan","BepCloud","cmetrics_diff","CustomBanaryScan","SQLReview","iasunittest","fossbot","FossBotMrScan","buildcheck","testcodechecker","eWindCloudExecute","sourcemeter"]
l =["checkstyle","simian","findbugs","sourcemonitor","sharpcounter","pmd","cobertura","sai","sloccount","compile","pygenie","sonarqube","uadpguarding","codedex","cseccheck","llt","codecc","Package","catchcheck","hutaf","duplicatefile","devtestc","agitar","nsiq","jslint","blackduck","flexelint","binaryfile","virusscan","devtest","deveco","ansiblelint","codecount","tslint","govet","envtest","devtestlcov","gocyclo","devtestjava","newcct","codecover","opensrcscan","eslint","scalastyle","jacoco","jshint","download","codecheck","codedexweb","buildmc","pylint","archguarding3","golint","androidlint","GoCover","jshint","CodeMars","sqlscan","CodeAnalyzer","Anystandard","Xmllint","Vlint","Vdiff","testBench","cmetrics","Canux","phoenixCA","pclint","phoenixlint","Xmllintlinux","gotest","codingstylecheck","devtestcGate","devtestlcovGate","buildmcenvcheck","compileOptionCheck","PythonTestcase","PylintScan","testcaseSpecification","jacoco","lltcov","pclintplus","lltcheck","sqlScan_CBGIT","strcheck","sqlScanCBGIT","gocycle","buildcheckDC","SecurityScan","BepCloud","cmetrics_diff","CustomBanaryScan","SQLReview","iasunittest","fossbot","FossBotMrScan","buildcheck","testcodechecker","eWindCloudExecute","sourcemeter"]

print(len(l))



