from typing import List

#Brute Force 
'''
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        # Brute force approach
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]
'''

#optimize solution

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n= len(nums) #size of list
        # use hash map to store value : index
        myMap = {}
        for i, n in enumerate(nums):
            different = target - n
            if different in myMap:# if we found solution
                return [myMap[different],i]
            #if we not find solution, need to update the hashmap
            myMap[n] = i
        return
            
        


def main():
    solution = Solution()

    # Example 1
    nums1, target1 = [2, 7, 11, 15], 9
    print("Input:", nums1, "Target:", target1)
    print("Output:", solution.twoSum(nums1, target1))  

    # Example 2
    nums2, target2 = [3, 2, 4], 6
    print("Input:", nums2, "Target:", target2)
    print("Output:", solution.twoSum(nums2, target2))  

    # Example 3
    nums3, target3 = [3, 3], 6
    print("Input:", nums3, "Target:", target3)
    print("Output:", solution.twoSum(nums3, target3))  



if __name__ == "__main__":
    main()
    
    