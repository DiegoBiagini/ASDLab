from graphs import *

def main():
    graph = create_weighted_graph(5, 0.8, 1, 10)
    print(graph)
    print(connected_components(graph))
    print(kruskal_algorithm(graph))



if __name__ == '__main__':
    main()