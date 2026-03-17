from collections import defaultdict
from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        #前缀和加上枚举👉维护左
        n=len(nums)
        pre=[0]*(n+1)
        ans=0
        for i in range(n+1):
            pre[i]=pre[i-1]+nums[i-1]
        cnt=defaultdict(int)
        for j in pre:
            ans+=cnt[j-k]
            cnt[j]+=1
        return ans
        