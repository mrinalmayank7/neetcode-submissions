class Solution:

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        result, left, right = [1]* n, [1]* n,[1]* n
        #at result [i] product is of subarray[:i] * [i+1:]
        #create a left product aarsy where left[i] is product of all elements on left
        #create a right product aarsy where right[i] is product of all elements on right
        #result[i] will be left[i]*right[i]
        for i in range(1,n):
            left[i] = left[i-1] * nums[i-1]#previous left product * number behind current
        for i in range(n-2,-1,-1):
            right[i] = right[i+1]* nums[i+1]
        for i in range(n):
            result[i]= left[i]*right[i]
       
        return result
        


    def productExceptSelfBrute(self, nums: List[int]) -> List[int]:
        result=[]
        for  i in range(len(nums)):
            product = 1
            for j in range(len(nums)):
                if j!=i:
                    product = product * nums[j]
            result.append(product)
        return result

        