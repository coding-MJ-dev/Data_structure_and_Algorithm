# 443. String Compression


class Solution:
    def compress(self, chars: List[str]) -> int:
        if len(chars) == 1:
            return 1
        i = 0
        j = 0
        while j < len(chars):
            chars[i] = chars[j]
            count = 1
            while j + 1 < len(chars) and chars[j + 1] == chars[i]:
                count += 1
                j += 1
            if count != 1:
                for c in str(count):
                    chars[i + 1] = c
                    i += 1
            i += 1
            j += 1

        return i
