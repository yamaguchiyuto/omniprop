import numpy as np
import scipy.sparse
from lib.mapping import Mapping

class OMNIProp:
    def __init__(self,graph,labels,labeled_nodes,lamb):
        self.labels = labels
        self.labeled_nodes = labeled_nodes
        self.label_map = Mapping(set(self.labels.values()))

        self.b = self.calc_prior(1.0)

        A = self.make_graph_matrix(graph) # np.array
        AU = A[len(self.labeled_nodes):,:]
        AL = A[:len(self.labeled_nodes),:]

        F = scipy.sparse.diags(np.array(1.0/((A.sum(0))+lamb))[0], 0)
        DU = scipy.sparse.diags(np.array(1.0/((A.sum(1).T)+lamb))[0][len(self.labeled_nodes):], 0)

        self.QUU = DU * AU * F * AU.T
        self.QUL = DU * AU * F * AL.T
        self.r = lamb * DU * (np.ones((len(self.labels)-len(self.labeled_nodes),1)) + AU * F * np.ones((len(self.labels),1)))

        self.SL = self.init_s()

    def make_graph_matrix(self,graph):
        graphM = scipy.sparse.lil_matrix((len(self.labels),len(self.labels)))
        for src in graph:
            for dst in graph[src]:
                graphM[src,dst] = 1
        return graphM.tocsr()

    def calc_prior(self,prior_strength):
        prior = np.zeros(len(self.label_map))
        v = prior_strength / len(labeled_nodes)
        for nid in labeled_nodes:
            lid = self.label_map.get_id(self.labels[nid])
            prior[lid] += v
        return prior

    def init_s(self):
        SL = scipy.sparse.lil_matrix((len(self.labeled_nodes), len(self.label_map)))
        for nid in self.labeled_nodes:
            lid = self.label_map.get_id(self.labels[nid])
            SL[nid,lid] = 1.
        return SL.tocsr()

    def run(self,th=0.001):
        E = self.QUL * self.SL
        c = self.r*self.b
        count = 0
        mincount = 10

        SU = np.zeros((len(self.labels)-len(self.labeled_nodes), len(self.label_map)))
        while True:
            new_SU = self.QUU * SU + E + c
            err = self.error(new_SU, SU)
            count += 1
            if err < th and count >= mincount:
                break
            SU = new_SU

        return SU

    def error(self,a,b):
        return np.abs(a-b).sum() / float(len(a))

if __name__ == '__main__':
    import sys
    import lib.util as util

    graphfile = sys.argv[1]
    labelsfile = sys.argv[2]
    lamb = float(sys.argv[3])

    graph = util.load_graph(graphfile)
    labels,labeled_nodes = util.load_labels(labelsfile)

    method = OMNIProp(graph,labels,labeled_nodes,lamb)
    result = method.run()
    inferred_labels = np.argmax(result,1)
    confidence = np.max(result,1)
    for n in range(len(inferred_labels)):
        label = method.label_map.get_value(int(inferred_labels[n]))
        print len(labeled_nodes)+n,label,float(confidence[n])
