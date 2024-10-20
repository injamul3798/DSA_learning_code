class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
       
        left = 0
        right = len(nums) - 1
        
        while left <= right:  # Loop until left crosses right
            mid = (left + right) // 2  # Calculate mid
            
            if nums[mid] == target:  # If target is found, return the index
                return mid
            elif (nums[mid] >= nums[left]):
                if nums[left]<=target<nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] < target<=nums[right]:
                     
                    left = mid + 1
                else:
                    right = mid - 1

        return -1