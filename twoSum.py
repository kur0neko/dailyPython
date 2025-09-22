from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        # Brute force approach
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]


def main():
    solution = Solution()

    # Example 1
    nums1, target1 = [2, 7, 11, 15], 9
    print("Input:", nums1, "Target:", target1)
    print("Output:", solution.twoSum(nums1, target1))  # [0, 1]

    # Example 2
    nums2, target2 = [3, 2, 4], 6
    print("Input:", nums2, "Target:", target2)
    print("Output:", solution.twoSum(nums2, target2))  # [1, 2]

    # Example 3
    nums3, target3 = [3, 3], 6
    print("Input:", nums3, "Target:", target3)
    print("Output:", solution.twoSum(nums3, target3))  # [0, 1]



if __name__ == "__main__":
    main()
    
    