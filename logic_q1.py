class Solution(object):
    def reverseNumber(self, nums):
        new = []
        for i in range(len(nums)):
            temp = str(nums[i])
            new.append(int(temp[1]+temp[0]))

        return new

if __name__ == '__main__':
    a = Solution()
    print(a.reverseNumber([53, 64, 75, 19, 92]))