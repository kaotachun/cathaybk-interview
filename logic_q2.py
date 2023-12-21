class Solution(object):
    def countCharacter(self, s):
        s = s.upper()
        d  = {}
        for char in s:
            if char == " ":
                continue
            if char in d.keys():
                d[char] = d[char] + 1
            else:
                d[char] = 1

        for key, value in sorted(d.items()):
            print (key + " " + str(value))


if __name__ == '__main__':
    a = Solution()
    a.countCharacter("Hello welcome to Cathay 60th year anniversary")