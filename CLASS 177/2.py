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
    initial_queue=deque([(start,[start])])
#    print(initial_queue)
    path=[]
    while initial_queue:
        current_node,current_path=initial_queue.popleft()
#        print(current_node)
#        current_path=initial_queue.popleft()
        for nearest in graph.get(current_node,[]):
            if nearest not in visited_node:
                visited_node.add(nearest)
                new_path=current_path+[nearest]
#                print(new_path)
                initial_queue.append((nearest,new_path))
                #print(initial_queue)
                #path.append(new_path)
    return new_path

all_path=bfs(graph,'Karachi')
#print(all_path)
for path in all_path:
   print(path)
