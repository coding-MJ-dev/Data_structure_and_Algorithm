# 929. Unique Email Addresses


class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        filtered = set()
        for e in emails:
            l, d = e.split("@")
            local = ""
            domain = d
            for i, c in enumerate(l):
                if c == ".":
                    continue
                elif c == "+":
                    break
                else:
                    local += c
            filtered.add(local + "@" + domain)
        # print(filtered)
        return len(filtered)
