class Solution:
    def findLengthOfLCIS(self, nums):
        if not nums:
            return 0

        max_len = 1
        current_len = 1

        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:  # если текущий элемент больше предыдущего
                current_len += 1
                max_len = max(max_len, current_len)
            else:
                current_len = 1  # сброс длины, если последовательность прерывается

        return max_len