class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs)==1 or len(strs)==0:
            return [strs]
        groups = defaultdict(list)
        for s in strs:
            key = tuple(sorted(s)) 
            groups[key].append(s)
        return list(groups.values())



        