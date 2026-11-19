class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        res = []
        candidates.sort()
        def backtrack(start: int, current_comb: list[int], remaining: int):
            if remaining == 0:
                res.append(list(current_comb))
                return
            for i in range(start, len(candidates)):
                if candidates[i] > remaining:
                    break
                current_comb.append(candidates[i])
                backtrack(i, current_comb, remaining - candidates[i])
                current_comb.pop()
        backtrack(0, [], target)
        return res