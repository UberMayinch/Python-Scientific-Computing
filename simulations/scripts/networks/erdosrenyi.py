import networkx as nx
import matplotlib.pyplot as plt

def erdos_renyi_random_network(n, gamma):
    # Calculate the probability parameter based on gamma parameter
    p = 2 * (n - 1) ** (-gamma)

    # Generate the Erdos-Renyi random graph
    G = nx.erdos_renyi_graph(n, p)

    return G

def main():
    # Define the number of nodes
    n = 100

    # Adjustable gamma parameter
    gamma = float(input("Enter the value of gamma parameter: "))

    # Generate the Erdos-Renyi random network
    G = erdos_renyi_random_network(n, gamma)

    # Plot the graph
    nx.draw(G, with_labels=True)
    plt.title(f"Erdos-Renyi Random Network with gamma = {gamma}")
    plt.show()

if __name__ == "__main__":
    main()
