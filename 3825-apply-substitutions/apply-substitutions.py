class Solution:
    def applySubstitutions(self, replacements: List[List[str]], text: str) -> str:
        rep_map = dict(replacements)

        while '%' in text:
            for (k, v) in rep_map.items():
                text = text.replace('%' + k + '%', v)
        
        return text