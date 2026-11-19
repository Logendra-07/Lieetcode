class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        N = {}
        d = []
        for i in range(1, n+1):
            for j in range(i+1, n+1):
                if i/j not in N:
                    N[i/j] = 1
                    d.append(f"{i}/{j}")
        return d