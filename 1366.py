from functools import cmp_to_key
class Solution:
    def rankTeams(self, votes: List[str]) -> str:
        stat = {i: [0] * len(votes[0]) for i in votes[0]}
        for vote in votes:
            for i in range(len(vote)):
                stat[vote[i]][i] += 1
        for i in stat:
            stat[i].append(i)
        return ''.join(i[-1] for i in sorted(stat.values(), key=cmp_to_key(lambda x, y: (1 if x > y else -1) if x[:-1] != y[:-1] else (1 if x[-1] < y[-1] else -1)), reverse=True))