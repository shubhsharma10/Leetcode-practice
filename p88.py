class Solution:
    def merge(self, nums1, m, nums2, n):
        e1 = m-1
        e2 = n-1
        curr = n+m-1
        while e1 >= 0 and e2 >= 0:
            if nums1[e1] > nums2[e2]:
                nums1[curr] = nums1[e1]
                e1 -= 1
                curr -= 1
            else:
                nums1[curr] = nums2[e2]
                e2 -= 1
                curr -= 1
        if e1 < 0 and e2 >= 0 and curr >= 0:
            while e2 >= 0:
                nums1[curr] = nums2[e2]
                e2 -= 1
                curr -= 1



st = Solution()
input_nums1 = [4,5,6,0]
input_nums2 = [10]
st.merge(input_nums1,3,input_nums2,1)
print(input_nums1)