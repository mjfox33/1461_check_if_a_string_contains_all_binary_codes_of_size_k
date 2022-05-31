class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        codes = set()
        for i in range(len(s) - k + 1):
            codes.add(bin(int(s[i:i+k],2)))
        return len(codes) == pow(2,k)