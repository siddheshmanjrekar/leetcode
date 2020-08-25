class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        return sum([1 for a in S if a in J])