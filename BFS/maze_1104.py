#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2020/11/4 11:34
# @Author : lantianyun l30001819
# @File : maze_1104.py


maze = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 1, 1, 1, 1, 1],
    [1, 0, 0, 1, 1, 1, 0, 1, 1, 1],
    [1, 0, 1, 1, 0, 1, 1, 1, 1, 1],
    [1, 0, 0, 1, 0, 0, 0, 0, 1, 1],
    [1, 0, 0, 1, 1, 0, 0, 0, 1, 1],
    [1, 1, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

def maze_path_queue(x1,y1,x2,y2):
    """
    :param x1: 起点横坐标
    :param y1: 起点纵坐标
    :param x2: 终点横坐标
    :param y2: 终点纵坐标
    :return: 路径
    """

    moves = [
        lambda x,y: (x,y-1),  #上
        lambda x,y: (x,y+1),  #下
        lambda x,y: (x-1,y),  #左
        lambda x,y: (x+1,y)   #右
    ]


    from _collections import deque
    q = deque()
    visited = []
    q.append((x1,y1,-1))
    visited.append((x1,y1,-1))

    while q:
        x,y,index = q.popleft()
        if (x,y) == (x2,y2):
            find_path(visited,index)
            return True
        visited.append((x, y,index))
        for move in moves:
            nextx,nexty = move(x,y)
            if maze[nextx][nexty] == 0:
                q.append((nextx,nexty,len(visited)-1))
                maze[x][y] = 2
    else:
        return False



def find_path(visited, index):
    if index != -1:
        find_path(visited, visited[index][2])
        print(visited[index][0], visited[index][1])


maze_path_queue(1,1,7,8)

