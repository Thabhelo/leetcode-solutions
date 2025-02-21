class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged = nums1 + nums2
        merged.sort()
        n = len(merged)
        
        if n % 2 == 0:
            mid = n // 2
            return (merged[mid - 1] + merged[mid]) / 2  # Average of two middle elements
        else:
            return merged[n // 2]  # Direct middle element

        