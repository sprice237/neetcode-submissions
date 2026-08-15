from collections import defaultdict

class CountSquares:
    def __init__(self):
        self.points_by_pos_y_int = defaultdict(list)
        self.points_by_neg_y_int = defaultdict(list)
        self.point_counts_by_point = defaultdict(int)

    def add(self, point: List[int]) -> None:
        x, y = point
        self.points_by_pos_y_int[y - x].append((x, y))
        self.points_by_neg_y_int[y + x].append((x, y))
        self.point_counts_by_point[(x, y)] = self.point_counts_by_point[(x, y)] + 1

    def count(self, point: List[int]) -> int:
        x1, y1 = point

        c = 0

        other_points_with_this_y_int = [x for x in self.points_by_pos_y_int[y1 - x1] if x != (x1, y1)] + [x for x in self.points_by_neg_y_int[y1 + x1] if x != (x1, y1)]

        for (x2, y2) in other_points_with_this_y_int:
            c += self.point_counts_by_point[(x1, y2)] * self.point_counts_by_point[(x2, y1)]

        return c