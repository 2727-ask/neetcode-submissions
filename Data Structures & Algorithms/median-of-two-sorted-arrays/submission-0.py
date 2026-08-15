class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums3 = nums1 + nums2
        nums3.sort()
        mid = len(nums3) // 2
        print(nums3)
        if(len(nums3) % 2 == 0):
            avg = (nums3[mid] + nums3[mid-1])/2
            return avg
        else:
            avg = nums3[mid]
            return avg