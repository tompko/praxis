import unittest

def winner(votes):
    vote_count = {}

    for v in votes:
        vote_count[v] = vote_count.get(v, 0) + 1

    majority = len(votes) / 2
    for v, c in vote_count.iteritems():
        if c > majority:
            return v

    return None

def confirm(votes, cand):
    vote_count = len([v for v in votes if v == cand])
    return vote_count > (len(votes) / 2)

def mjrty(votes):
    cand = None
    k = 0

    for v in votes:
        if k == 0:
            cand = v
            k = 1
        elif v == cand:
            k += 1
        else:
            k -= 1

    if confirm(votes, cand):
        return cand
    return None

class TestMajorityVoting(unittest.TestCase):
    def test_winner(self):
        votes = [(["A","B","A","B","A"], "A"),
                 (["A","A","A","C","C","B","B","C","C","C","B","C","C"], "C"),
                 (["A","B","C","A","B","A"], None)]
        for v in votes:
            self.assertEquals(winner(v[0]), v[1])

    def test_mjrty(self):
        votes = [(["A","B","A","B","A"], "A"),
                 (["A","A","A","C","C","B","B","C","C","C","B","C","C"], "C"),
                 (["A","B","C","A","B","A"], None)]
        for v in votes:
            self.assertEquals(mjrty(v[0]), v[1])

if __name__ == "__main__":
    unittest.main()
