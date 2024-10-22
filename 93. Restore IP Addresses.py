# 93. Restore IP Addresses


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        if len(s) < 4 or len(s) > 12:
            return []
        if len(s) == 4:
            return [".".join(s)]
        ans = []

        def split(s, cur):
            # print(s, cur)
            if len(cur) > 4:
                return
            if not s and len(cur) == 4:
                ans.append(".".join(cur[:]))
                return
            # 뒤에서 부터 3개 뺀, 혹은 1개 뺀, 맨앞이 영이 아니면 컬 앞에 추가 한뒤에 dfs 보
            for i in range(0, min(len(s), 4)):

                cut = s[: i + 1]
                # print(s, i, cur)
                if 0 <= int(cut) < 256:
                    if str(int(cut)) == cut:
                        split(s[i + 1 :], cur + [cut])

        split(s, [])
        return ans
