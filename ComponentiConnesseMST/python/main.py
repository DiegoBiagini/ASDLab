import pickle
import sys
from timeit import default_timer as timer

import matplotlib.pyplot as plt

from graphs import *


def main():
    min_weight = 1
    max_weight = 10
    max_tree_height = 2000

    np.set_printoptions(threshold=sys.maxsize)

    # Sizes of the graphs that will be tested, max size will be around 4k nodes
    sizes = [2**i for i in range(0, 13)]

    # Probabilities of node presence that will be tested
    probs = [0.2, 0.4, 0.6, 0.8, 1]

    # Data that will be used to compile graphs
    # Each entry of the dictionary(key is p) contains a list of tuples (size, time, nccs) for the connected components
    # For kruskal each tuple is (size, time, tweight, height), if not possible everything will be None
    cc_data = {p: [] for p in probs}
    krusk_data = {p: [] for p in probs}

    for size in sizes:
        for p in probs:
            file_name = "size=" + str(size) + "_p=" + str(p).replace(".", "") + ".dat"
            graph = create_weighted_graph(size, p, min_weight, max_weight)

            # Save to file
            with open("data/in_" + file_name, "wb") as f:
                pickle.dump(graph, f)

            time_connected = timer()
            ccs = connected_components(graph)
            time_connected = timer() - time_connected

            print("Size=" + str(size) + ", p=" + str(p))
            print("Connected components:" + str(len(ccs)) + " Time:" + str(time_connected))

            cc_data[p].append((size, time_connected, len(ccs)))

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

                if size < max_tree_height:
                    # Calculate mst height(minimum of all possible bfs-es)
                    mst_graph = create_graph_from_arcs(size, mst)
                    for i in range(0, size):
                        bfs_max_time = BFS_max(mst_graph, i)
                        if bfs_max_time < mst_height:
                            mst_height = bfs_max_time
                else:
                    mst_height = ""

                print("Kruskal successful, MST height:" + str(mst_height) + ", MST_weight:" + str(mst_weight)
                      + " Time:" + str(time_kruskal))
                krusk_data[p].append((size, time_kruskal, mst_weight, mst_height))
            else:
                print("Kruskal not possible")
                krusk_data[p].append((size, None, None, None))

            with open("data/out_cc_" + file_name, "wb") as f:
                pickle.dump(ccs, f)

            if len(ccs) == 1:
                with open("data/out_mst_" + file_name, "wb") as f:
                    pickle.dump(mst, f)

    with open("data/cc_overall.dat", "wb") as f:
        pickle.dump(cc_data, f)
    with open("data/mst_overall.dat", "wb") as f:
        pickle.dump(krusk_data, f)

    for p in probs:
        plt.clf()

        # Size-time ccs
        plt.plot([rec[0] for rec in cc_data[p]], [rec[1] for rec in cc_data[p]])
        plt.suptitle("Tempo di ricerca delle componenti connesse per p=" + str(p))
        plt.xlabel("Size")
        plt.ylabel("Time(s)")
        plt.savefig("../plots/cc_time_p=" + str(p).replace(".", "") + ".png")

        # Size-Number of ccs
        plt.clf()

        plt.plot([rec[0] for rec in cc_data[p]], [rec[2] for rec in cc_data[p]])
        plt.suptitle("Numero di componenti connesse per p=" + str(p))
        plt.xlabel("Size")
        plt.ylabel("Componenti connesse")
        plt.savefig("../plots/cc_number_p=" + str(p).replace(".", "") + ".png")

        # Size-time Kruskal
        plt.clf()

        plt.plot([rec[0] for rec in krusk_data[p] if rec[1] is not None],
                 [rec[1] for rec in krusk_data[p] if rec[1] is not None])
        plt.suptitle("Tempo di ricerca MST per p=" + str(p))
        plt.xlabel("Size")
        plt.ylabel("Time(s)")
        plt.savefig("../plots/krusk_time_p=" + str(p).replace(".", "") + ".png")

        # Size-Weight Kruskal
        plt.clf()

        plt.plot([rec[0] for rec in krusk_data[p] if rec[1] is not None],
                 [rec[2] for rec in krusk_data[p] if rec[1] is not None])
        plt.suptitle("Peso totale MST per p=" + str(p))
        plt.xlabel("Size")
        plt.ylabel("Weight")
        plt.savefig("../plots/krusk_Weight_p=" + str(p).replace(".", "") + ".png")

        # Size-height Kruskal
        plt.clf()

        plt.plot([rec[0] for rec in krusk_data[p] if rec[0] < max_tree_height and rec[1] is not None],
                 [rec[3] for rec in krusk_data[p] if rec[0] < max_tree_height and rec[1] is not None])
        plt.suptitle("Altezza MST per p=" + str(p))
        plt.xlabel("Size")
        plt.ylabel("Height")
        plt.savefig("../plots/krusk_height_p=" + str(p).replace(".", "") + ".png")


if __name__ == '__main__':
    main()