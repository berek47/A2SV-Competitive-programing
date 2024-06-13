class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        k_set, v_set = set(), set()
        for x, y in edges:
            k_set.add(x)
            v_set.add(y)
        res = []
        for k in k_set:
            if k not in v_set:
                res.append(k)
        return res
