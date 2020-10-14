#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2020/10/13 19:06
# @Author : lantianyun l30001819
# @File : maze.py


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

dirs =[
    lambda x,y:(x+1,y),  # →
    lambda x,y:(x-1,y),  # ←
    lambda x,y:(x,y-1),  # ↑
    lambda x,y:(x,y+1)   # ↓
]

from collections import deque  # 用队列来实现
def maze_path_queue(x1,y1,x2,y2):
    """
    :param x1: 起点横坐标
    :param y1: 起点纵坐标
    :param x2: 终点横坐标
    :param y2: 终点纵坐标
    :return: 路径
    """

    visited = []
    startNode = (x1,y1,-1) # 前两位表示横纵坐标，第3位表示这个节点是由谁引入的，这个值是visited的下标，通过这个下标可以最终找到路径
    q = deque()
    q.append(startNode) # 将起点放入队列

    while q:  # 队列为空则循环结束
        popNode = q.popleft()  # 出队,注意这里用双端队列的popleft，先入先出。千万不要写成pop了，pop是后入先出，等同于栈
        if (popNode[0],popNode[1]) == (x2,y2): # 找到了终点
            find_path(visited, popNode[2])  # 然后打印出路径，也就是visit中的节点
            return True
        visited.append(popNode) # 出队的节点同时放入已访问的节点
        for dir in dirs:
            nextNode =dir(popNode[0],popNode[1])
            if maze[nextNode[0]][nextNode[1]] == 0 :
                q.append((nextNode[0],nextNode[1],len(visited)-1))
                maze[nextNode[0]][nextNode[1]] = 2 # 标记为已近访问过这个节点

    else: #如果队列为空还没找到路，就认为没有路
        print("没有路")
        return False





def find_path(visited,index):
    if index != -1:
        find_path(visited,visited[index][2])
        print(visited[index][0],visited[index][1])

    # else:
    #     print(visited[index][0], visited[index][1])

maze_path_queue(1,1,7,8)

