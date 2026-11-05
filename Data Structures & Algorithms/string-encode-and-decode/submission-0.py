class Solution:

    def encode(self, strs: List[str]) -> str:
        return "".join(f"{len(s)}#{s}" for s in strs)

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0

        while i < len(s):
            separator = s.index("#", i)
            length = int(s[i:separator])

            start = separator + 1
            end = start + length
            result.append(s[start:end])

            i = end

        return result
