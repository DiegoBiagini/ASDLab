from graphs import *

def main():
    graph = create_graph(4, 0.5)
    print(graph)
    graph = create_weighted_graph(5, 0.3, 1, 10)
    print(graph)
    for i in range(0, 5):
        print(adjacent_nodes(graph, i))



if __name__ == '__main__':
    main()