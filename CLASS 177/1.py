from collections import deque
graph = {
    'Karachi': ['Clifton', 'Saddar', 'Gulshan', 'Korangi'],
    'Clifton': ['DHA', 'Sea View'],
    'Saddar': ['Tower', 'Empress Market'],
    'Gulshan': ['Gulshan-e-Iqbal', 'Nipa'],
    'Korangi': ['Landhi', 'Shah Faisal'],
    'DHA': ['Khyaban-e-Ittehad', 'Beach Park'],
    'Gulshan-e-Iqbal': ['University Road', 'National Stadium'],
    'Landhi': ['Industrial Area', 'Cattle Colony'],
    'Shah Faisal': ['Airport', 'Malir'],
    'Tower': ['Quaid Mausoleum'],
    'Empress Market': ['Burns Road'],
    'National Stadium': ['Hassan Square']
}

def bfs(graph, start):
    visited_node=set()
    initial_queue=deque([start])
    while initial_queue:
        initial_node=initial_queue.popleft()
        if initial_node not in visited_node:
            print(initial_node,end=' - > ')
            visited_node.add(initial_node)
            initial_queue.extend(nearest for nearest in graph.get(initial_node,[]) if nearest not in visited_node)
bfs(graph,'Karachi')
