class Solution:
    def buddyStrings(self, A, B):
        A_len = len(A)
        B_len = len(B)
        if A_len != B_len :
            return False
        else:
            if A_len < 2:
                return False
            else:
                mismatched = []
                dup = {}
                mismatchCount = 0
                for i in range(A_len):
                    if A[i] != B[i]:
                        mismatchCount += 1
                        mismatched.append((A[i],B[i]))
                    if A[i] in dup:
                        dup[A[i]] += 1
                    else:
                        dup[A[i]] = 1
                print(dup)
                if mismatchCount == 0:
                    for key in dup:
                        if dup[key] > 1:
                            return True
                        return False
                elif mismatchCount == 2:
                    if mismatched[0][0] == mismatched[1][1] and mismatched[0][1] == mismatched[1][0]:
                        return True
                    else:
                        return False
                else:
                    return False

st = Solution()
print(st.buddyStrings("aa","aa"))