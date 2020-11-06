#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2020/11/4 19:43
# @Author : lantianyun l30001819
# @File : mem.py

from sys import stdin


# If you need to import additional packages or classes, please import here.


class MiniMemoryPool:
    # 返回分配的内存首地址(string)，失败返回字符串 "error"
    def __init__(self):
        self.mem = [[0, 99, 0]]

    def request(self, size: int) -> str:
        '''
        请求
        :param size:
        :return:
        '''
        if size <= 0:
            return "error"
        for i in range(len(self.mem)):
            begin, end, used = self.mem[i]
            if used == 1:
                continue
            if end - begin + 1 >= size:
                self.mem.pop(i)
                self.mem.insert(i, [begin, begin + size - 1, 1])
                if end - begin + 1 > size:
                    self.mem.insert(i + 1, [begin + size, end, 0])
                return begin
        else:
            return "error"
        return ""

    # 成功返回 true；失败返回 false，失败时框架会自动输出 "error"
    def release(self, start_addr: int) -> bool:
        # 在此补充你的代码
        max_index = len(self.mem) - 1
        for i in range(max_index+1):
            begin, end, used = self.mem[i]
            if begin == start_addr and used == 1:
                self.mem[i][2] = 0  # 修改使用标志
                if i - 1 >= 0:
                    pre_begin, pre_end, pre_used = self.mem[i - 1]
                if i + 1 <= max_index:
                    next_begin, next_end, next_used = self.mem[i + 1]

                if i - 1 >= 0 and pre_used == 0 and \
                        pre_end == begin - 1:
                    # 与前一空闲区间合并
                    begin = pre_begin
                    self.mem[i - 1] = "pre"  # 弹出前一区间
                if i + 1 <= max_index and next_used == 0 and \
                        next_begin == end + 1:
                    # 与后一空闲区间合并
                    end = next_end
                    self.mem[i + 1] = "next"
                self.mem[i] = [begin, end, 0]
                if "pre" in self.mem:
                    self.mem.remove("pre")
                if "next" in self.mem:
                    self.mem.remove("next")
                return True
        else:
            return False
        return False


if __name__ == "__main__":
    commands = ["REQUEST=10", "REQUEST=20", "RELEASE=10", "REQUEST=30", "RELEASE=0", "REQUEST=20", "RELEASE=60"]
    command_count = len(commands)
    pool = MiniMemoryPool()
    for commandline in commands:
        command, size = commandline.strip().split("=")
        if command == "REQUEST":
            print(pool.request(int(size)))
            print(pool.mem)
        elif command == "RELEASE":
            released = pool.release(int(size))
            print(pool.mem)
            if not released:
                print("error")

