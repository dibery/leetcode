class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder, ans, pos = sorted(i + '/' for i in folder), [], 0
        while pos < len(folder):
            new = pos + 1
            ans.append(folder[pos][:-1])
            while new < len(folder) and folder[new].startswith(folder[pos]):
                new += 1
            pos = new
        return ans
