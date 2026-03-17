from typing import List
class Solution:
    def rob(self, nums: List[int]) -> int:
        # @cache
        # def dfs(i)->int:
        #     if i<0:
        #         return 0
        #     return max(dfs(i-2)+nums[i],dfs(i-1))
        # return dfs(len(nums)-1)
        n=len(nums)
        dp=[0]*(n+2)
        for i in range(n):
            dp[i+2]=max(dp[i]+nums[i],dp[i+1])
        return dp[-1]


        