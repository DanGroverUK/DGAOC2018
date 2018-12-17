import networkx as nx

#-------Read in the input-----#

steps = []
with open("input.txt", mode="r") as inp:
    for line in inp:
        data = {'step': line[5], 'before': line[36]}
        steps.append(data)

# Main loop:
graph = nx.DiGraph()
for a in steps:
    graph.add_edge(a['step'], a['before'])

sorted_graph = nx.lexicographical_topological_sort(graph)
answer = ""
for a in sorted_graph:
    answer = answer + a

print("Answer: {}".format(answer))
