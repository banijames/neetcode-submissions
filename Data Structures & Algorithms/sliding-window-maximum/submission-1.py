class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
       left = 0
       res=[]
       for right in range(len(nums)):
           if right-left+1==k:
            new=max(nums[left:right+1])
            res.append(new)
            left+=1
       return res
