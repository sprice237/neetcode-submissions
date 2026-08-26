class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        num_steps = len(cost)
        memoed_min_cost = [-1] * num_steps

        def min_cost_from_step(step):
            if step >= num_steps:
                return 0
            
            min_cost = memoed_min_cost[step]
            if min_cost >= 0:
                return min_cost

            min_cost = cost[step] + min(min_cost_from_step(step + 2), min_cost_from_step(step + 1))
            memoed_min_cost[step] = min_cost
            return min_cost

        return min(min_cost_from_step(1), min_cost_from_step(0))