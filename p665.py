
class Solution:
    def checkPossibility(self, nums):
        negindex = []
        for i in range(len(nums)-1):
            if nums[i+1] < nums[i]:
                negindex.append(i+1)

        print(negindex)


        if len(negindex) == 0:
            return True
        elif len(negindex) > 1:
            return False
        elif len(negindex) == 1:
            if negindex[0] == len(nums)-1:
                return True
            elif negindex[0] == 1:
                if nums[0] > nums[1]:
                    return True
                else:
                    if nums[2] < nums[0]:
                        return False
                    else:
                        return True

            else:
                curIndex = negindex[0]
                if nums[curIndex+1] < nums[curIndex-1]:
                    return False
                else:
                    return True
        return False




input_array = [-1, 4, 2, 3]
st = Solution()
canPass = st.checkPossibility(input_array)
print(canPass)