"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals = sorted(intervals, key=lambda x: x.start)

        for i in range(1, len(intervals)):
            a = intervals[i - 1]
            b = intervals[i]

            if b.start < a.end:
                return False

        return True