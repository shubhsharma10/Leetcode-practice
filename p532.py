class Solution:
    def findDupPairs(self,nums):
        nums_set = set(nums)
        dup = 0
        for x in nums_set:
            dup_item = nums.count(x)
            if dup_item > 1:
                dup += 1
        return dup

    def findPairs(self, nums, k):
        if k == 0:
            return self.findDupPairs(nums)
        else:
            dup = 0
            nums_set = set(nums)
            for x in nums_set:
                y = x + k
                if y in nums_set:
                    dup += 1
            return dup

st = Solution()
input_nums = [1,3,1,5,4]
input_k = -2
print(st.findPairs(input_nums, input_k))