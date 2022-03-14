class Solution:
    def simplifyPath(self, path: str) -> str:
        import re
        path = re.sub('/*$', '', path)
        path = re.sub('/+', '/', path)
        pos = []
        for p in path[1:].split('/'):
            if p == '.':
                pass
            elif p == '..':
                if pos:
                    pos.pop()
            else:
                pos.append(p)
        return '/' + '/'.join(pos)
