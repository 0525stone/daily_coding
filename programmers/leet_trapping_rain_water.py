"""
Given n non-negative integers representing an elevation map where the width of each bar is 1,
   compute how much water it can trap after raining.


Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1].
In this case, 6 units of rain water (blue section) are being trapped.

result

Runtime: 2332 ms, faster than 5.01% of Python3 online submissions for Trapping Rain Water.
Memory Usage: 14.9 MB, less than 37.18% of Python3 online submissions for Trapping Rain Water.

"""
from typing import *

class Solution:
    def trap(self, height: List[int]) -> int:

        water = 0
        _flag = 0

        high = 0
        high_i = 0

        for i, h in enumerate(height):

            if(h):
                if(_flag==0):
                    high = h     # 이 변수는 없어도 될 뻔 height[i]
                    high_i = i
                    _flag = 1
                    continue

                if(high<=h):
                    water = water + (i-high_i-1)*high - sum(height[high_i+1:i])
                    for j in range(high_i+1,i):    # 만약 리스트의 끝이 넘을수도 있는 상황에서 -1 말고 방법이 있나?
                        height[j] = high
                    high = h
                    high_i = i

                else:            # high 보단 짧은 h 만났을 때,
                    check_h = 0
                    for j in range(high_i+1,i):  # height counting
                        if(height[j]>h):
                            check_h = check_h + h
                        else:
                            check_h = check_h + height[j]

                    if((i-high_i-1)*h  < check_h):
                        continue
                    else:
                        water = water + (i-high_i-1)*h- check_h
                        for k in range(high_i+1,i):
                            if(height[k]<h):
                                height[k] = h
            print(height, water)


        return water






height = [0,1,0,2,1,0,1,3,2,1,2,1] # 6
# height = [4,2,0,3,2,5] # 9
# height = [5,4,1,2] # 1
# print(sum(height[1:4]))
water = Solution()
water_ = water.trap(height)
print(water_)