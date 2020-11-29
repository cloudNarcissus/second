#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2020/11/27 9:15
# @Author : lantianyun l30001819
# @File : 621_leastInterval.py


# 输入：tasks = ["A","A","A","B","B","B"], n = 2
# 输出：8
# 解释：A -> B -> (待命) -> A -> B -> (待命) -> A -> B

from typing import List

from collections import Counter, deque, OrderedDict

tasks = ["A", "A", "A", "B", "B", "B", "C", "C", "C", "D", "D", "E"]

# 下面给出的前两种方法都是错的...

class Solution:
    def __init__(self):
        self.q = deque()
        self.res = []
        self.task_counter = OrderedDict()

    def leastInterval(self, tasks: List[str], n: int) -> int:
        self.task_counter = OrderedDict(Counter(tasks))

        while self.task_counter:

            for task, cnt in self.task_counter.items():  # 注意对字典遍历一定要加items()
                if task in self.q:
                    continue
                elif task not in self.q:
                    self.intoDeque(n, task)
                    break
            else:
                self.intoDeque(n, "None")

        return self.res

    def intoDeque(self, n, task):
        if len(self.q) < n:
            self.q.append(task)
        elif len(self.q) == n > 0:
            self.q.popleft()
            self.q.append(task)
        elif len(self.q) == n == 0:
            pass
        self.res.append(task)
        self.counterClear(task)

    def counterClear(self, task):
        if task != "None":
            self.task_counter[task] -= 1
            if self.task_counter[task] == 0:
                self.task_counter.pop(task)


class Solution2:
    def __init__(self):
        self.q = deque()
        self.res = []
        self.task_counter = OrderedDict()
        self.tasks = []

    def leastInterval(self, tasks: List[str], n: int) -> int:
        self.taskOrder(tasks)
        while self.tasks:
            for task in self.tasks:
                if task in self.q:
                    continue
                elif task not in self.q:
                    self.intoDeque(n, task)
                    break
            else:
                self.intoDeque(n, "None")

        return self.res

    def intoDeque(self, n, task):
        if len(self.q) < n:
            self.q.append(task)
        elif len(self.q) == n > 0:
            self.q.popleft()
            self.q.append(task)
        elif len(self.q) == n == 0:
            pass
        self.res.append(task)
        if task != "None":
            self.tasks.remove(task)

    def counterClear(self, task):
            self.task_counter[task] -= 1
            if self.task_counter[task] == 0:
                self.task_counter.pop(task)


    def taskOrder(self,tasks):
        l = [(task,cnt) for task, cnt in Counter(tasks).items()]
        l.sort(key=lambda x:x[1], reverse=True)
        for item in l:
            self.task_counter[item[0]] = item[1]

        while self.task_counter:
            for task in list(self.task_counter.keys()):
                self.tasks.append(task)
                self.counterClear(task)


class Solution3:
    def __init__(self):
        self.res = []

    def leastInterval(self, tasks: List[str], n: int) -> int:

        tasks_cnt = [[task, cnt] for task, cnt in Counter(tasks).items()]

        while tasks_cnt:
            self.fetchnLargest(tasks_cnt, n)
            tasks_cnt = [[task, cnt] for task, cnt in tasks_cnt if cnt>0]  # 一定不要在遍历列表的时候pop
            tasks_cnt.sort(key=lambda x:x[1], reverse=True)

        while self.res[-1] == "None":
            self.res.pop()

        return len(self.res)

    def fetchnLargest(self,task_cnt, n):
        for i in range(n+1):
            if i <= len(task_cnt)-1:
                task_cnt[i][1] -= 1
                self.res.append(task_cnt[i][0])
            elif i > len(task_cnt)-1 :
                self.res.append("None") # 放空闲


# 优先队列（堆）

from heapq import heapify, heappush, heappop
class Solution4:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        tasks_cnt = [[-1*cnt, task] for task, cnt in Counter(tasks).items()]  # 数字放在前面便于堆的默认排序
        heapify(tasks_cnt)
        res = 0

        # 每一轮取n+1个任务，然后数量+1（因为之前乘以了负号），如果不为0则放回堆中，直到堆为空
        while tasks_cnt:
            temp = []
            for i in range(n+1):
                if tasks_cnt:
                    [cnt, task] = heappop(tasks_cnt)
                    cnt += 1
                    if cnt < 0:
                        temp.append([cnt, task])
                elif not tasks_cnt and not temp:
                    break
                res += 1
            for [cnt, task] in temp:
                heappush(tasks_cnt, [cnt, task])
        return res




# tasks = ["A","A","A","B","B","B"]
tasks =["E","A", "A", "A", "B", "B", "B", "C", "C", "C", "D", "D", "E"]
s = Solution3()
s.leastInterval(tasks, 2)

s4 = Solution4()
print(s4.leastInterval(tasks, 2))