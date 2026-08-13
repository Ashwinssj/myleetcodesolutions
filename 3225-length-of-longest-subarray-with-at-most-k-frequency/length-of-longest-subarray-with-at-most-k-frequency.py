class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        fre={}
        left=0
        ans=0

        for right in range(len(nums)):
            if nums[right] in fre:
                fre[nums[right]]+=1
            else:
                fre[nums[right]]=1

            while fre[nums[right]]>k:
                fre[nums[left]]-=1
                left+=1
            
            ans=max(ans,right-left+1)
        
        return ans

        