class Solution(object):
    def circleCount(self, n):
        p = [i+1 for i in range(n)]
        k = 0
        while len(p) > 1:
            i = 0
            while i < len(p):
                k = k + 1
                if k == 3:
                    del p[i]
                    k = 0
                else:
                    i = i + 1
        return p


if __name__ == '__main__':
    a = Solution()
    n = int(input())
    print(a.circleCount(n))