from bisect import bisect_left

class Solution:
    def suggestedProducts(self, word: List[str], query: str) -> List[List[str]]:
        word, ans = sorted(word), []
        for i in range(len(query)):
            ans.append([])
            pos = bisect_left(word, query[:i + 1])
            for j in range(3):
                try:
                    if word[pos + j].startswith(query[:i + 1]):
                        ans[-1].append(word[pos + j])
                except:
                    break
        return ans
