class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        n=len(height)
        ltr=[0]*n
        rtl=[0]*n
        ltr[0]=height[0]
        rtl[n-1]=height[n-1]
        for i in range(1,n):
            ltr[i]=max(ltr[i-1],height[i])
        for j in range(n-2,-1,-1):
            rtl[j]=max(rtl[j+1],height[j])
        total=0
        for i in range(n):
            total+=(min(ltr[i],rtl[i])-height[i])
        return total        
        