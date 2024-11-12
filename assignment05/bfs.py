import numpy as np
import matplotlib.pyplot as plt
import networkx as nx

def SpMV(rptA, cidA, x, y):
    y[:] = np.zeros_like(y)
    for i in range(len(rptA) - 1):
        y[i] = np.sum(x[cidA[rptA[i]:rptA[i+1]]])
    y[y != 0] = 1

def BFS(rpt, cid, start_node):
    x = np.zeros(m)
    y = np.zeros(m)
    x[start_node] = 1

    node_colors[start_node] = 'lightgreen'
    edge_colors = ['black'] * len(G.edges)

    plt.clf()
    nx.draw(G, pos, with_labels=True, edge_color=edge_colors, node_color=node_colors, node_size=500)
    plt.pause(1)

    loop_num = 0
    while True:
        print('level', loop_num, ':')
        loop_num += 1
        SpMV(rpt, cid, x, y)

        xid = np.where(x == 1)[0]
        yid = np.where(y == 1)[0]
        print('vector x:', x, '->input:', xid)
        print('vector y:', y, '->output:', yid)

        if np.sum(y) == 0:
            edge_colors = ['black'] * len(G.edges)
            plt.clf()
            nx.draw(G, pos, with_labels=True, edge_color=edge_colors, node_color=node_colors, node_size=500)
            plt.pause(1)
            break
        else:
            for i in xid:
                temp = 0
                for j, edge in enumerate(G.edges):
                    if edge[0] == i:
                        edge_colors[temp] = 'red'
                    temp += 1
            for i in yid:
                node_colors[i] = 'lightgreen'
            plt.clf()
            nx.draw(G, pos, with_labels=True, edge_color=edge_colors, node_color=node_colors, node_size=500)
            plt.pause(1)

            x = y
            y = np.zeros(m)

def readGraphfile():
    with open(filename, 'r') as f:
        m, n, num = map(int, f.readline().split())
        adj_matrix = np.zeros((m, n))
        for line in f.readlines():
            src, dst = map(int, line.split())
            adj_matrix[dst][src] = 1
    return m, n, num, adj_matrix

if __name__ == '__main__':
    filename = input("Please input the graph file name:")

    print('Read file and create the adjacency matrix...')
    m, n, num, adj_matrix = readGraphfile()
    print('The size (n) of the adjacency matrix:', n)
    print('The number of nonzeros (nnz) in the adjacency matrix:', num)
    print('')

    csrRowPtr = np.zeros(m + 1, dtype=int)
    csrColIdx = np.zeros(num, dtype=int)
    cooRowIdx = np.zeros(num, dtype=int)
    cooColIdx = np.zeros(num, dtype=int)
    nnz_ptr = 0

    for i in range(m):
        csrRowPtr[i + 1] = csrRowPtr[i] + np.sum(adj_matrix[i] == 1)
        indices = np.where(adj_matrix[i] == 1)[0]
        csrColIdx[nnz_ptr:nnz_ptr+len(indices)] = indices
        cooRowIdx[nnz_ptr:nnz_ptr+len(indices)] = i
        cooColIdx[nnz_ptr:nnz_ptr+len(indices)] = indices
        nnz_ptr += len(indices)
    print('===================================')
    print('Coordinate (COO) format:')
    print('RowIdx:', cooRowIdx)
    print('ColIdx:', cooColIdx)
    print('The total length of COO format data: len(RowIdx) + len(ColIdx) -> nnz + nnz ->', len(cooRowIdx) + len(cooColIdx))
    print('')

    print('===================================')
    print('Compressed Sparse Row (CSR) format:')
    print('RowPtr:', csrRowPtr)
    print('ColIdx:', csrColIdx)
    print('The total length of CSR format data: len(RowPtr) + len(ColIdx) -> (n + 1) + nnz ->', len(csrRowPtr) + len(csrColIdx))

    G = nx.DiGraph()
    G.add_nodes_from(range(m))
    edges = [(csrColIdx[j], i) for i in range(m) for j in range(csrRowPtr[i], csrRowPtr[i + 1])]
    G.add_edges_from(edges)
    pos = nx.shell_layout(G)

    node_colors = ['grey'] * len(G.nodes)
    edge_colors = ['black'] * len(G.edges)

    plt.figure()
    nx.draw(G, pos, with_labels=True, edge_color=edge_colors, node_color=node_colors, node_size=500)

    print('===================================')
    print('Breadth First Search (BFS) Process:')
    start_node = 0
    BFS(csrRowPtr, csrColIdx, start_node)

    plt.show()