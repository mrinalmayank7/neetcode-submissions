class Solution:
    #most optimal, store directly left and right in result
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        result= [1]* n
        for i in range(1,n):
            result[i] = result[i-1] * nums[i-1]#previous left product * number behind current
        right_product = 1
        for i in range(n-1,-1,-1):
            result[i] = result[i]* right_product
            right_product = right_product * nums[i]
       
        return result
        


    def productExceptSelfOptimal(self, nums: List[int]) -> List[int]:
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


"""
Brute:        O(n²) time  O(1) space  ← two nested loops
O(n) space:   O(n)  time  O(n) space  ← left + right arrays, readable
O(1) space:   O(n)  time  O(1) space  ← optimal, one variable for right


Core idea for all approaches:
result[i] = product of everything LEFT of i × product of everything RIGHT of i


APPROACH 1 — Brute O(n²) O(1):
For every index i — loop through entire array skipping i, multiply everything else.
Simple but redundant — same numbers multiplied again and again for each index.


APPROACH 2 — Left+Right Arrays O(n) O(n):
Instead of recomputing left and right products repeatedly — precompute once and store.

Build left array:
left[current value] = product of all left elements = prev left product * last num
eg:[
nums = [3,8,2,1]
left = [1,1,1,1] -> [1,1*3, 1*3*8, 1*3*8*2] 
left = [1, 3, 24, 48]

Build right array:
opposite of just left

Multiply:
result[i] = left[i] (product of left side of i) × right[i] (product of right side of i)
Why O(n) space: storing two extra arrays of size n.


APPROACH 3 — Space Optimized O(n) O(1):
Observation from Approach 2: 
we need left[i] and right[i] at same time only during final multiplication. 
Can we avoid storing both?

Left part — store directly in result:
Result array IS the left array. No separate left array needed.

Right part — why we don't need right array:
In Approach 2 right array was built and stored. 
But during multiplication we use right[i] only ONCE at index i, then never again.
means right_product is a product multiplication var : 1* (right product 1) * (right product 2)
now result to be left * current right product

nums   = [1,  2,  3,  4]
result = [1,  1,  2,  6]   ← after left pass

right_product=1, go right to left:

i=3: result[3] = 6 × 1  = 6,  right_product = 1×4  = 4
i=2: result[2] = 2 × 4  = 8,  right_product = 4×3  = 12
i=1: result[1] = 1 × 12 = 12, right_product = 12×2 = 24
i=0: result[0] = 1 × 24 = 24, right_product = 24×1 = 24

result = [24,12,8,6] 


"""