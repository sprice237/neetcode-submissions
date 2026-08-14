class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []

        merged_intervals = []
        intervals.sort()

        i = 0
        j = 1

        mi_start, mi_end = intervals[0]

        for i_start, i_end in intervals[1:]:
            if i_start > mi_end:
                merged_intervals.append([mi_start, mi_end])
                mi_start, mi_end = i_start, i_end
            else:
                mi_end = max(mi_end, i_end)

        merged_intervals.append([mi_start, mi_end])

        return merged_intervals