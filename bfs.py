from collections import deque


def bfs(graph, start_key, finish_key):
    search_queue = deque()
    search_queue += graph[start_key]
    visited = []

    while search_queue:
        vertex = search_queue.popleft()
        if vertex not in visited:
            if vertex == finish_key:
                return True
            else:
                search_queue += graph[vertex]
                visited.append(vertex)
    return False


if __name__ == '__main__':
    graph = dict()
    graph['I'] = ['Vasya', 'Sasha']
    graph['Vasya'] = ['Lena']
    graph['Lena'] = ['Olya']
    graph['Olya'] = ['Anya']
    graph['Sasha'] = ['Vasya', 'Olya', 'Grisha']
    graph['Grisha'], graph['Anya'] = [], []

    if bfs(graph, 'I', 'Anya'):
        print('There is a path from me to Anya')
