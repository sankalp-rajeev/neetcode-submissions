class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:

        def dfs(i):
            visited[i] = True
            # [[1,1,0],[1,1,0]]
            for neighbour,connected in enumerate(isConnected[i]):
                if connected and not visited[neighbour]:
                    dfs(neighbour)


        numCities = len(isConnected)
        visited = [False]*numCities
        province_count = 0
        for i in range(numCities):
            if not visited[i]:
                dfs(i)
                province_count += 1
        return province_count
