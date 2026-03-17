from functools import cache
from typing import List
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        #找到子数组的和为sum//2
        n=len(nums)
        t=sum(nums)//2
        if  sum(nums)%2:
            return False
        #表示前i个数字能不能选出一个子数组使和为t
        @cache
        def dfs(i,j)->bool:
            if i<0:
                return True if j==0 else False
            if nums[i]>j:
                return dfs(i-1,j)
            return dfs(i-1,j) or dfs(i-1,j-nums[i])
        return dfs(n-1,t)
        

        