from typing import List

class Solution:
    def twoSumDistant(self, nums: List[int], target: int) -> List[int]:
        self.value_x = 0
        self.value_y = 0
        self.target = target
        self.nums = nums
        self.output_Distant = []
        for x in range(len(self.nums)):
            for y in range(len(self.nums)):
                if self.nums[x] + self.nums[y] == self.target:
                    self.output_Distant.append(self.value_x)
                    self.output_Distant.append(self.value_y)
                    return self.output_Distant
                self.value_y += 1
            self.value_x += 1
            self.value_y = 0




hello = Solution()
# print(hello.twoSum([4,3,4,7,8,5,4],9))
print(hello.twoSumDistant([4,6,7,5,8],15))