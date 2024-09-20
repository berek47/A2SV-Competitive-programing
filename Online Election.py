class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        n = len(times)
        self.topCandidate = deque()
        self.times = times
        currentVotes = defaultdict(lambda: 0)
        currentMax = 0

        for i in range(n):
            votedPerson = persons[i]
            currentVotes[votedPerson] += 1
            currentPersonVotes = currentVotes[votedPerson]
            if currentPersonVotes >= currentMax:
                self.topCandidate.append(persons[i])
                currentMax = currentPersonVotes   
            else:
                currentTop = self.topCandidate[-1]
                self.topCandidate.append(currentTop)

    def q(self, t: int) -> int:
        upperBound = bisect_right(self.times, t)
        return self.topCandidate[upperBound-1]
