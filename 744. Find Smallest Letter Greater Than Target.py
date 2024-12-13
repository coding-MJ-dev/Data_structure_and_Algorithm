# 744. Find Smallest Letter Greater Than Target

class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        idx = bisect.bisect_right(letters, target)
        
        return letters[idx] if len(letters) != idx else letters[0]