from collections import deque, defaultdict

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        connections_by_source = defaultdict(list)

        for (ui, vi, ti) in times:
            connections_by_source[ui].append((ui, vi, ti))

        final_times = {(x + 1): -1 for x in range(n)}

        q = deque([(k, 0)])
        
        def bfs():
            node, total_time = q.popleft()

            if final_times[node] > -1 and final_times[node] <= total_time:
                return

            final_times[node] = total_time
            connections = connections_by_source[node]

            for (ui, vi, ti) in connections:
                q.append((vi, total_time + ti))

        while q:
            bfs()

        if -1 in final_times.values():
            return -1

        return max(final_times.values())

        