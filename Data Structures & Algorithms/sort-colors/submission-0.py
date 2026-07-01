class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        2,1,0,1,2
        bucket[2]++
        bucket[1]++
        bucket[0]++
        bucket[1]++
        bucket[2]++
        bucket = [1,2,2]
        """
        bucket_size=3 #max is 2 2+1=3
        bucket=[0]*bucket_size #create bucket [0,0,0]
        
        for i in nums:
            bucket[i] +=1
        i=0
        for value in range(len(bucket)):
            for j in range(bucket[value]):
                nums[i]=value
                i+=1



