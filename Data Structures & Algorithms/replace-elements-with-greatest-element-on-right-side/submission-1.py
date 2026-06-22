class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        if not arr:
            return arr
        last_index=len(arr)-1
        current_max=arr[last_index]
        arr[last_index]=-1
        for i in range(last_index-1,-1,-1):
            new_max = max(current_max, arr[i]) 
            arr[i] = current_max
            current_max=new_max
        return arr
        

"""
Input: arr = [2,4,5,3,1,2]
current_max=2
arr = [2,4,5,3,1,-1]
loop from second last to first element
new_max = (current_max, current_element) = (2,1)=2
arr = [2,4,5,3,current_max,-1]= [2,4,5,3,2,-1]
current_max=new_max=2

new_max = (current_max, current_element) = (2,3)=3
arr = [2,4,5,current_max,2,-1]= [2,4,5,2,2,-1]
current_max=new_max=3

new_max = (current_max, current_element) = (3,5)=5
arr = [2,4,current_max,2,2,-1]= [2,4,3,2,2,-1]
current_max=new_max=5

new_max = (current_max, current_element) = (5,4)=5
arr = [2,current_max,3,2,2,-1]= [2,5,3,2,2,-1]
current_max=new_max=5

new_max = (current_max, current_element) = (5,2)=5
arr = [current_max,5,3,2,2,-1]= [5,5,3,2,2,-1]
current_max=new_max=5

"""

"""
brute force 
    def replaceElements(self, arr: List[int]) -> List[int]:
        arr_length=len(arr)
        for i in range(arr_length-1):
            arr_max_subset=arr[i+1:arr_length]
            print(arr_max_subset)
            arr[i] = max(arr_max_subset)
        arr[arr_length-1]=-1
        return arr

arr = [2,4,5,3,1,2]
arr_length = 6
i = 0, arr[0] = max(arr[1:6])
"""
        