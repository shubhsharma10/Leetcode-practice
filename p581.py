class Solution:
    def findUnsortedSubarray(self, nums):
        nums_length = len(nums)
        if nums_length < 2:
            return 0
        else:
            sorted_nums = sorted(nums)
            print(sorted_nums)
            begin = 0
            end = nums_length - 1
            while begin < end:
                moved = False
                if nums[begin] == sorted_nums[begin]:
                    begin += 1
                    moved = True
                if nums[end] == sorted_nums[end]:
                    end -= 1
                    moved = True
                if not moved:
                    return end - begin + 1
            return 0




st = Solution()
input_nums = [2,6,4,8,10,9,15]
print(st.findUnsortedSubarray(input_nums))
