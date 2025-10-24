class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        num = n + 1
        while True:
            if self.is_balanced(num):
                return num
            num += 1

    def is_balanced(self, num: int) -> bool:
        count = {}
        for ch in str(num):
            count[ch] = count.get(ch, 0) + 1
        for ch, freq in count.items():
            if ch == '0' or freq != int(ch):
                return False
        return True