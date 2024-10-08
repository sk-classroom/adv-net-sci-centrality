# %% Import
from scipy import sparse
import pandas as pd
import igraph
import numpy as np

node_table = pd.read_csv(
    "https://raw.githubusercontent.com/skojaku/adv-net-sci-course/main/data/airport_network_v2/node_table.csv"
)
edge_table = pd.read_csv(
    "https://raw.githubusercontent.com/skojaku/adv-net-sci-course/main/data/airport_network_v2/edge_table.csv"
)
src, trg = tuple(edge_table[["src", "trg"]].values.T)
edge_list = tuple(zip(src, trg))

# node_id and name dictionary
n_nodes = node_table.shape[0]
id2name = np.array([""] * n_nodes, dtype="<U64")
id2name[node_table["node_id"]] = node_table["Name"].values

g = igraph.Graph(
    edge_list,
    vertex_attrs=dict(Name=id2name, node_id=node_table["node_id"].values),
)


# %% Test -----------
topk_closeness_answer = ['Frankfurt Main', 'Charles De Gaulle', 'Heathrow', 'Schiphol', 'Dubai Intl']

topk_closeness = top_k_closeness_centrality(g, 5)

assert set(topk_closeness) == set(topk_closeness_answer), "The top-k closeness centrality results do not match the expected answer."

