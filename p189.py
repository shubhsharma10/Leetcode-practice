class Solution:
    def rotate(self, nums, k):
        nums_length = len(nums)
        k = k % nums_length
        if nums_length > 1 and k > 0:
            start_index = nums_length-k
            new_array = nums[nums_length-k:nums_length]
            for i in range(start_index):
                reverse_i = start_index - i - 1
                new_position = reverse_i + k
                nums[reverse_i], nums[new_position] = nums[new_position], nums[reverse_i]
            for i in range(len(new_array)):
                nums[i] = new_array[i]


st = Solution()
input_array = [1,2,3,4,5,6,7]
input_k = 3
print("Input")
print(input_array)
st.rotate(input_array, input_k)
print("Output")
print(input_array)