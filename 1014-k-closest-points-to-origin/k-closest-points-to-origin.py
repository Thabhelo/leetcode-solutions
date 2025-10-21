class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # key = squared Euclidean distance from origin
        # return heapq.nsmallest(k, points, key=lambda p: p[0]*p[0] + p[1]*p[1])

        def dist(x, y):
            return math.sqrt(x**2 + y**2)

        heap = []
        for x, y in points:
            d = dist(x, y)
            if len(heap) < k:
                heapq.heappush(heap, (-d, x, y))
            else: 
                heapq.heappushpop(heap, (-d, x, y))

        return [(x, y) for d, x, y in heap]

        # O(n log k) time and O(k) space
