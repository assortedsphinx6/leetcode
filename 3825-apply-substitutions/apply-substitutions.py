class Solution:
    def applySubstitutions(self, replacements: List[List[str]], text: str) -> str:
        mapping = {k: v for k, v in replacements}
        pattern = re.compile(r'%([A-Z])%')

        # Keep substituting until no placeholders remain
        while pattern.search(text):
            text = pattern.sub(lambda m: mapping[m.group(1)], text)

        return text
