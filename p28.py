class Solution:
    def strStr(self, haystack, needle):
        needle_len = len(needle)
        haystack_len = len(haystack)
        if needle_len == 0:
            return 0
        ptr1 = 0
        ptr2 = 0
        matchedYet = 0
        while ptr2 < haystack_len:
            if needle[ptr1] == haystack[ptr2]:
                if ptr1 == needle_len - 1:
                    return ptr2 - needle_len + 1
                else:
                    ptr1 += 1
                    ptr2 += 1
                    matchedYet += 1
            else:
                if matchedYet > 0:
                    ptr2 = ptr2 - matchedYet + 1
                else:
                    ptr2 += 1
                ptr1 = 0
                matchedYet = 0
        return -1

st = Solution()
print(st.strStr("mississipi","issip"))
