# Graph Analysis Project: Facebook Social Network

A small project for an algorithms course, analyzing the SNAP Facebook social network dataset using Python and the NetworkX library.

## Project Overview

This project implements several graph algorithms to uncover structural properties of the network, identify influential nodes, and detect communities.

The analysis is performed on the [Facebook dataset from SNAP](https://snap.stanford.edu/data/egonets-Facebook.html), which consists of 4,039 nodes and 88,234 edges, representing an anonymized network of user friendships.

## Analysis Performed

1.  **Basic Statistics:** Calculated the total number of nodes, edges, and the average degree to understand the network's density.
2.  **Shortest Paths:** Computed the average shortest path length ("degrees of separation") for the network.
3.  **Centrality Analysis:** Identified influential nodes:
    * **Degree Centrality:** To find "hubs" (nodes with the most connections).
    * **Betweenness Centrality:** To find "bridges" (nodes that connect different parts of the network).
4.  **Community Detection:** Used the **Louvain method** to partition the graph into distinct communities or "friend circles."
5.  **Visualization:** Generated and saved a plot of the largest detected community to the `visualizations/` folder.

## How to Run

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/bjoern555/graph-analysis-project.git](https://github.com/bjoern555/graph-analysis-project.git)
    cd graph-analysis-project
    ```

2.  **Set up a virtual environment and install dependencies:**
    ```bash
    # Create the environment
    python -m venv .venv
    
    # Activate it (Windows)
    .venv\Scripts\activate
    # (On Linux/macOS: source .venv/bin/activate)
    
    # Install required libraries
    pip install networkx matplotlib scipy
    ```

3.  **Run the analysis script:**
    ```bash
    python analysis.py
    ```

## Example Output

This is the output from running `analysis.py`.

Basic Graph Info:
Number of nodes: 4039
Number of edges: 88234
Average degree: 43.69

Shortest Path Analysis:
Average shortest path length: 3.69

Centrality Analysis:
Top 5 Nodes by Degree (Most connected):
  Node 107 with 1045 connections
  Node 1684 with 792 connections
  Node 1912 with 755 connections
  Node 3437 with 547 connections
  Node 0 with 347 connections

Betweenness Centrality:

Top 5 Nodes by Betweenness (Best 'bridges'):
  Node 107 with score: 0.4871
  Node 1684 with score: 0.3206
  Node 3437 with score: 0.2433
  Node 1912 with score: 0.2282
  Node 0 with score: 0.1671

Community Detection using Louvain method:

Found 16 communities.

Top 5 largest communities:
  Community 0: 548 members
  Community 1: 535 members
  Community 2: 435 members
  Community 3: 433 members
  Community 4: 423 members

Visualizing:
Preparing visualization of the largest community...
Graph visualization saved to: visualizations/largest_community.png