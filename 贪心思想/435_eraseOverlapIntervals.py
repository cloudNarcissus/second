
# 输入: [ [1,2], [2,3], [3,4], [1,3] ]
# 删除最少区间数，使得不重叠


from typing import List

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:x[1])  # 按照结束时间排序

        result = []  # 存储保留的区间

        for interval in intervals:
            if result:
                if interval[0]>=result[-1][1]: # 如果下一个区间的开始时间比已存在的时间大，则满足条件，否则就是时间区域重叠
                    result.append(interval)
            else:
                result.append(interval)

        return  len(result)
