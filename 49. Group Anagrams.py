# 49. Group Anagrams

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
       seen = defaultdict(list)

        for s in strs:
            sort = ''.join(sorted(s))
            seen[sort].append(s)
        
        return list(seen.values())