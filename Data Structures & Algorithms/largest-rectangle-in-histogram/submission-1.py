class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area=0
        stk=[]
        n=len(heights)
        for i,height in enumerate(heights):
            start=i
            while stk and height< stk[-1][0]:
                h,j=stk.pop()#finding there is shorter graph
                w=i-j
                a=h*w
                max_area=max(max_area,a)
                start=j
            stk.append((height,start))
        while stk:
            h,j=stk.pop()
            w=n-j
            max_area=max(max_area,h*w)
        return max_area