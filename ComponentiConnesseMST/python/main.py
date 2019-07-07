import sys
from timeit import default_timer as timer

from graphs import *


def main():
    min_weight = 1
    max_weight = 10

    np.set_printoptions(threshold=sys.maxsize)

    # Sizes of the graphs that will be tested, max size will be around 8k nodes
    sizes = [2**i for i in range(0, 14)]

    # Probabilities of node presence that will be tested
    probs = [0.2, 0.4, 0.6, 0.8, 1]

    for size in sizes:
        for p in probs:
            file_name = "size=" + str(size) + "_p=" + str(p) + ".txt"
            graph = create_weighted_graph(size, p, min_weight, max_weight)

            # Save to file
            with open("data/in_" + file_name, "w") as f:
                print(graph, file=f)

            time_connected = timer()
            ccs = connected_components(graph)
            time_connected = timer() - time_connected

            print("Size=" + str(size) + ", p=" + str(p))
            print("Connected components:" + str(len(ccs)) + " Time:" + str(time_connected))

            # Perform kruskal if possible
            mst_height = np.inf
            mst_weight = 0
            time_kruskal = 0
            mst = None

            if len(ccs) == 1:
                time_kruskal = timer()
                mst = kruskal_algorithm(graph)
                time_kruskal = timer() - time_kruskal

                # Calculate total mst weight
                for el in mst:
                    mst_weight += el[0]

                # Calculate mst height(minimum of all possible bfs-es)
                mst_graph = create_graph_from_arcs(size, mst)
                for i in range(0, size):
                    bfs_max_time = BFS_max(mst_graph, i)
                    if bfs_max_time < mst_height:
                        mst_height = bfs_max_time


                print("Kruskal successful, MST height:" + str(mst_height) + ", MST_weight:" + str(mst_weight)
                      + " Time:" + str(time_kruskal))
            else:
                print("Kruskal not possible")

            print()

            with open("data/out_" + file_name, "w") as f:
                print(ccs, file=f)
                if len(ccs) == 1:
                    print(mst, file=f)




if __name__ == '__main__':
    main()