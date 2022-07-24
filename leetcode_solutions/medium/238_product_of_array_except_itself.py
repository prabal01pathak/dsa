class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        x = 1
        zeros = 0
        for i in nums:
            x *= i 
            if i == 0:
                zeros+=1
        if zeros > 1:
            return [0]*len(nums)
        product_arr = []
        for i in range(len(nums)):
            if nums[i] == 0:
                p = 1
                for j in range(len(nums)):
                    if i == j:
                        continue
                    p *= nums[j]
            else:
                p = x/nums[i]
            
            product_arr.append(int(p))
        return product_arr

                               
           
