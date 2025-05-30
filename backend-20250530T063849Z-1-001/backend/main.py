from fastapi import FastAPI, Body
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Dict, Any
import networkx as nx

# Models for request data
class PipelineData(BaseModel):
    nodes: List[Dict[str, Any]]
    edges: List[Dict[str, Any]]

# Create FastAPI app
app = FastAPI()

# Add CORS middleware to allow cross-origin requests from frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins in development
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods
    allow_headers=["*"],  # Allow all headers
)

@app.get('/')
def read_root():
    return {'Ping': 'Pong'}

@app.post('/pipelines/parse')
def parse_pipeline(pipeline_data: PipelineData):
    # Extract nodes and edges from request
    nodes = pipeline_data.nodes
    edges = pipeline_data.edges
    
    # Count nodes and edges
    num_nodes = len(nodes)
    num_edges = len(edges)
    
    # Check if the graph is a DAG (Directed Acyclic Graph)
    is_dag = check_is_dag(nodes, edges)
    
    return {
        'num_nodes': num_nodes,
        'num_edges': num_edges,
        'is_dag': is_dag
    }

def check_is_dag(nodes, edges):
    """
    Check if the given nodes and edges form a Directed Acyclic Graph (DAG).
    A DAG is a directed graph with no cycles.
    """
    # Create a directed graph
    G = nx.DiGraph()
    
    # Add nodes to the graph
    for node in nodes:
        G.add_node(node['id'])
    
    # Add edges to the graph
    for edge in edges:
        source = edge['source']
        target = edge['target']
        G.add_edge(source, target)
    
    # Check if the graph contains cycles
    try:
        # If the graph has cycles, this will raise NetworkXUnfeasible
        nx.find_cycle(G)
        return False  # Has cycles, not a DAG
    except nx.NetworkXNoCycle:
        return True  # No cycles, is a DAG
