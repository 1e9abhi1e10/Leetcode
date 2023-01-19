class Solution:
    def subarraysDivByK(self, A: List[int], K: int) -> int:
        res = 0
        prefix = 0
        count = [1] + [0] * K
        for a in A:
            prefix = (prefix + a) % K
            res += count[prefix]
            count[prefix] += 1
        return res
        
        