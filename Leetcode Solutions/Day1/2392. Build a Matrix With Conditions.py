class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:

        def topo(cond):
            adj = [[] for _ in range(k)]
            indegree = [0] * k

            for i, j in cond:
                adj[i - 1].append(j - 1)
                indegree[j - 1] += 1
            queue = deque()
            for i in range(len(indegree)):
                if indegree[i] == 0:
                    queue.append(i)
            ans = []
            while queue:
                node = queue.pop()
                ans.append(node + 1)

                for neigh in adj[node]:
                    indegree[neigh] -= 1
                    if indegree[neigh] == 0:
                        queue.append(neigh)
            return ans

        row = topo(rowConditions)
        col = topo(colConditions)
        if len(row) < k or len(col) < k:
            return []
        ans = [[0] * k for _ in range(k)]
        row = {x: i for i, x in enumerate(row)}
        col = {x: j for j, x in enumerate(col)}

        for kal in range(1, k + 1):
            ans[row[kal]][col[kal]] = kal
        return ans

