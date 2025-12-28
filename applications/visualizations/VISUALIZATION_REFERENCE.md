# Visualization Techniques Reference

Quick reference for creating visualizations of data structures and algorithms in Python.

---

## 1. Graphviz (Trees & Graphs)

**Best for:** Binary trees, graphs, tries, linked lists
**Effort:** 15-30 minutes
**Install:** `pip install graphviz pydot`

### Example: Binary Tree Visualization

```python
from graphviz import Digraph

def visualize_tree(root, filename='tree'):
    """Visualize a binary tree structure"""
    dot = Digraph()

    def add_nodes(node):
        if node:
            dot.node(str(id(node)), str(node.val))
            if node.left:
                dot.edge(str(id(node)), str(id(node.left)))
                add_nodes(node.left)
            if node.right:
                dot.edge(str(id(node)), str(id(node.right)))
                add_nodes(node.right)

    add_nodes(root)
    dot.render(filename, view=True, format='png')

# Usage:
# visualize_tree(root)
```

### Example: Graph Visualization

```python
from graphviz import Graph

def visualize_graph(adjacency_list, filename='graph'):
    """Visualize an undirected graph from adjacency list"""
    dot = Graph()

    for node, neighbors in adjacency_list.items():
        dot.node(str(node))
        for neighbor in neighbors:
            dot.edge(str(node), str(neighbor))

    dot.render(filename, view=True, format='png')

# Usage:
# graph = {0: [1, 2], 1: [0, 3], 2: [0, 3], 3: [1, 2]}
# visualize_graph(graph)
```

---

## 2. Print-Based (Quick Terminal Viz)

**Best for:** Debugging, understanding algorithm steps, quick iteration
**Effort:** 5 minutes
**Install:** None (built-in)

### Example: Array State with Highlighting

```python
def visualize_array(arr, highlight=None, label=""):
    """Print array with optional highlighted indices"""
    output = f"{label}: [" if label else "["

    for i, val in enumerate(arr):
        if highlight and i in highlight:
            output += f" >{val}< "
        else:
            output += f" {val} "
    output += "]"
    print(output)

# Usage:
# visualize_array([1,3,5,7,9], highlight=[2], label="Step 3")
# Output: Step 3: [ 1  3  >5<  7  9 ]
```

### Example: Two-Pointer Visualization

```python
def visualize_two_pointers(arr, left, right):
    """Visualize two-pointer technique"""
    output = "["
    for i, val in enumerate(arr):
        if i == left and i == right:
            output += f" >{val}< "
        elif i == left:
            output += f" L{val} "
        elif i == right:
            output += f" R{val} "
        else:
            output += f" {val} "
    output += "]"
    print(output)

# Usage during algorithm:
# visualize_two_pointers([1,2,3,4,5], left=0, right=4)
# Output: [ L1  2  3  4  R5 ]
```

### Example: Binary Tree Print

```python
def print_tree(root, level=0, prefix="Root: "):
    """Print tree structure in terminal"""
    if root:
        print(" " * (level * 4) + prefix + str(root.val))
        if root.left:
            print_tree(root.left, level + 1, "L--- ")
        if root.right:
            print_tree(root.right, level + 1, "R--- ")

# Output example:
# Root: 5
#     L--- 3
#         L--- 1
#         R--- 4
#     R--- 7
#         L--- 6
```

---

## 3. Matplotlib (Animations & Plots)

**Best for:** Sorting algorithms, array manipulations, DP tables
**Effort:** 1-2 hours first time, 30 min after
**Install:** `pip install matplotlib`

### Example: Animate Sorting Algorithm

```python
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def visualize_sorting(arr, steps):
    """
    Animate sorting process

    Args:
        arr: initial array
        steps: list of array states at each step
    """
    fig, ax = plt.subplots()
    ax.set_title("Sorting Visualization")

    bar_rects = ax.bar(range(len(arr)), arr, align="edge")
    ax.set_xlim(0, len(arr))
    ax.set_ylim(0, int(1.1 * max(arr)))

    iteration = [0]

    def update_fig(arr_state):
        for rect, val in zip(bar_rects, arr_state):
            rect.set_height(val)
        iteration[0] += 1
        ax.set_title(f"Sorting - Step {iteration[0]}")

    anim = animation.FuncAnimation(
        fig,
        update_fig,
        frames=steps,
        interval=500,
        repeat=False
    )

    plt.show()

# Usage:
# Modify your sorting algorithm to yield states:
# def bubble_sort_with_states(arr):
#     steps = [arr.copy()]
#     for i in range(len(arr)):
#         for j in range(len(arr) - i - 1):
#             if arr[j] > arr[j + 1]:
#                 arr[j], arr[j + 1] = arr[j + 1], arr[j]
#                 steps.append(arr.copy())
#     return steps
#
# steps = bubble_sort_with_states([5, 2, 8, 1, 9])
# visualize_sorting([5, 2, 8, 1, 9], steps)
```

### Example: Visualize DP Table

```python
import matplotlib.pyplot as plt
import numpy as np

def visualize_dp_table(dp_table, title="DP Table"):
    """Visualize 2D DP table as heatmap"""
    fig, ax = plt.subplots()

    im = ax.imshow(dp_table, cmap='YlOrRd')
    ax.set_title(title)

    # Add text annotations
    for i in range(len(dp_table)):
        for j in range(len(dp_table[0])):
            text = ax.text(j, i, dp_table[i][j],
                          ha="center", va="center", color="black")

    plt.colorbar(im, ax=ax)
    plt.show()

# Usage:
# dp = [[0,1,1,1], [1,1,2,2], [1,2,2,3]]
# visualize_dp_table(dp, "Longest Common Subsequence")
```

---

## 4. NetworkX (Graph Algorithms)

**Best for:** Graph traversal, pathfinding, graph algorithms
**Effort:** 1-2 hours
**Install:** `pip install networkx matplotlib`

### Example: Visualize Graph Traversal

```python
import networkx as nx
import matplotlib.pyplot as plt

def visualize_bfs(graph, start_node, traversal_order):
    """
    Visualize BFS traversal step by step

    Args:
        graph: dict of adjacency list
        start_node: starting node
        traversal_order: list of nodes in visit order
    """
    G = nx.Graph(graph)
    pos = nx.spring_layout(G)

    plt.figure(figsize=(10, 6))

    for i, current_node in enumerate(traversal_order):
        plt.clf()

        # Color nodes: visited (red), current (green), unvisited (lightblue)
        node_colors = []
        for node in G.nodes():
            if node == current_node:
                node_colors.append('green')
            elif node in traversal_order[:i]:
                node_colors.append('red')
            else:
                node_colors.append('lightblue')

        nx.draw(G, pos, node_color=node_colors,
                with_labels=True, node_size=700, font_size=16)
        plt.title(f"BFS Traversal - Step {i+1}: Visiting {current_node}")
        plt.pause(1)

    plt.show()

# Usage:
# graph = {0: [1, 2], 1: [0, 3, 4], 2: [0, 5], 3: [1], 4: [1], 5: [2]}
# order = [0, 1, 2, 3, 4, 5]  # BFS order from node 0
# visualize_bfs(graph, 0, order)
```

### Example: Static Graph with Path Highlighted

```python
import networkx as nx
import matplotlib.pyplot as plt

def visualize_path(graph, path, title="Path Visualization"):
    """Highlight a path in a graph"""
    G = nx.Graph(graph)
    pos = nx.spring_layout(G)

    # Draw all edges in gray
    nx.draw_networkx_edges(G, pos, edge_color='gray', width=1)

    # Draw path edges in red
    path_edges = [(path[i], path[i+1]) for i in range(len(path)-1)]
    nx.draw_networkx_edges(G, pos, edgelist=path_edges,
                          edge_color='red', width=3)

    # Draw nodes
    node_colors = ['red' if node in path else 'lightblue' for node in G.nodes()]
    nx.draw_networkx_nodes(G, pos, node_color=node_colors, node_size=700)
    nx.draw_networkx_labels(G, pos, font_size=16)

    plt.title(title)
    plt.axis('off')
    plt.show()

# Usage:
# graph = {0: [1, 2], 1: [0, 3], 2: [0, 3], 3: [1, 2, 4], 4: [3]}
# path = [0, 1, 3, 4]  # Path from 0 to 4
# visualize_path(graph, path, "Shortest Path: 0 -> 4")
```

---

## 5. Advanced Options (Future Reference)

### Pygame
**Best for:** Custom interactive visualizations, pathfinding demos
**Install:** `pip install pygame`
**Effort:** 3-5 hours per visualization
**Use case:** Create interactive sorting visualizer, A* pathfinding demo

### Manim (3Blue1Brown style)
**Best for:** Explaining concepts, teaching animations
**Install:** `pip install manim`
**Effort:** 5-10 hour learning curve
**Use case:** Beautiful explanatory videos for portfolio

---

## Quick Decision Guide

| What to Visualize | Recommended Tool | Why |
|-------------------|------------------|-----|
| Binary Tree structure | Graphviz | Clean diagrams, minimal code |
| Array during sorting | Print-based OR matplotlib | Print for debugging, matplotlib for portfolio |
| Graph structure | NetworkX OR Graphviz | NetworkX for algorithms, Graphviz for structure |
| BFS/DFS traversal | NetworkX | Built for graph algorithms |
| Two pointers/sliding window | Print-based | Quick and effective |
| DP table states | matplotlib heatmap | Shows patterns in table |
| Recursion tree | Graphviz | Clear hierarchical structure |
| Linked list | Print-based OR Graphviz | Print usually sufficient |

---

## Tips

1. **Start simple:** Print-based visualizations are often enough for understanding
2. **Save for portfolio:** Use matplotlib/NetworkX for 2-3 impressive demos
3. **Don't over-visualize:** Visualization is a tool for learning, not the goal
4. **Iterate:** Start with print, upgrade to graphical if needed
5. **Test incrementally:** Visualize at each step during algorithm development

---

*Last updated: 2025-12-28*
