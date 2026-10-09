# """
# This is HtmlParser's API interface.
# You should not implement it, or speculate about its implementation
# """
#class HtmlParser(object):
#    def getUrls(self, url):
#        """
#        :type url: str
#        :rtype List[str]
#        """

class Solution:
    def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> List[str]:

        visited = set()
        def bfs(n):
            queue = deque()
            queue.append(n)
            visited.add(n)
            while queue:
                node = queue.popleft()
                for nei in htmlParser.getUrls(node):
                    if nei not in visited and nei.split('/')[2]==node.split('/')[2]:
                        queue.append(nei)
                        visited.add(nei)
        bfs(startUrl)
        return list(visited)
        