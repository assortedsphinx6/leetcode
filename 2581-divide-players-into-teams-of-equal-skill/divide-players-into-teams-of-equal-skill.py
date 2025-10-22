class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        l, r = 0, len(skill) - 1
        target = skill[l] + skill[r]
        chem = 0

        while l < r:
            if skill[l] + skill[r] != target:
                return -1
            chem += skill[l] * skill[r]
            l += 1
            r -= 1
        return chem

            

