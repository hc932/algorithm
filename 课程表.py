from collections import deque
from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        #拓扑排序的思路？
        """
        先用g建一个图
        用before记录每个节点的前驱的个数
        再维护一个队列
        这个队列左端出去的都是前驱变成0的
        每左出队一个就加到答案里面
        """
        #[1,0]   ->    0->1   必须先修0课程
        #建图
        g=[[] for _ in range(numCourses)]
        before=[0]*numCourses
        for x,y in prerequisites:
            g[y].append(x)
            before[x]+=1#记录节点的前驱个数，就是记录有几个数字指向它
        q=deque(i for i,x in enumerate(before) if x==0)
        ans=[]
        while q:
            #维护双端队列
            l=q.popleft()
            ans.append(l)
            for i in g[l]:
                before[i]-=1
                if before[i]==0:
                    q.append(i)
        if len(ans)<numCourses:
            return []
        return ans 
            
            


        


        
        