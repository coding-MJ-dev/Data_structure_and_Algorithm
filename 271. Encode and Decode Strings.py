# 271. Encode and Decode Strings


class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string."""
        # words = strs.spilt()
        return "\n".join(strs)

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings."""
        # print(s)
        words = s.split("\n")
        return words
