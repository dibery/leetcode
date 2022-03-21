class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        parse = ''
        score = 0
        for c in s:
            parse += c
            if parse.count('(') * 2 == len(parse):
                score += Solution.scoreOfParentheses(self, parse[1:-1]) * 2 if parse != '()' else 1
                parse = ''
        return score
