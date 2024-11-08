class Solution:
    def intersection(self, nums1, nums2):
        # Используем множества для нахождения пересечений
        set1 = set(nums1)
        set2 = set(nums2)
        return list(set1 & set2)
