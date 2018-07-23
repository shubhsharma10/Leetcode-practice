class Solution:
    def thirdMax(self, nums):
        nums = set(nums)
        nums_length = len(nums)
        print(nums)
        if nums_length < 3:
            return max(nums)
        else:
            nums.remove(max(nums))
            nums.remove(max(nums))
            return max(nums)

st = Solution()
input_nums = [3,4,5,1,2,2,1]
print(st.thirdMax(input_nums))