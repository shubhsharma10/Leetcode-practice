class Solution:
    def canPlaceFlowers(self, flowerbed, n):
        count = 0
        flowerbed_len = len(flowerbed)
        if flowerbed_len == 0:
            return False
        elif flowerbed_len == 1:
            count = flowerbed.count(0)
        elif flowerbed_len == 2:
            count = flowerbed.count(0)
            if count < 2:
                count = 0
            else:
                count = 1
        else:
            for i in range(flowerbed_len):
                before = 0
                after = 0
                if i == 0:
                    after = i+1
                    if flowerbed[after] == 0 and flowerbed[i] == 0:
                        count += 1
                        flowerbed[i] = 1
                elif i == len(flowerbed) - 1:
                    before = i-1
                    if flowerbed[before] == 0 and flowerbed[i] == 0:
                        count += 1
                        flowerbed[i] = 1
                else:
                     if flowerbed[i] == 0 and flowerbed[i-1] == 0 and flowerbed[i+1] == 0:
                        count += 1
                        flowerbed[i] = 1
        return n <= count

st = Solution()
input_flowerbed_1 = [1]
input_n = 1
print(st.canPlaceFlowers(input_flowerbed_1,input_n))