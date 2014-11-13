import sys

def load_labels(filename,delim=' '):
    labels = {}
    labeled_nodes = set([])
    for line in open(filename):
        nid,label = map(int,line.rstrip().split(delim))
        labels[nid] = label
        if label != -1:
            labeled_nodes.add(nid)
    return (labels,labeled_nodes)

def load_graph(filename,delim=' '):
    graph = {}
    for line in open(filename):
        src,dst = map(int,line.rstrip().split(delim))
        if not src in graph: graph[src] = set([])
        graph[src].add(dst)
    return graph
