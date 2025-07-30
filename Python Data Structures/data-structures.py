import numpy as np

class Graph_Node:
    def __init__(self, id:str):
        self.id = id
        self.neighbors = []
        self.visited = False
    
    def add_neighbor(self, other:'Graph_Node'):
        """Adds a neighbor to the graph node, as if the graph were undirected."""
        if other not in self.neighbors:
            self.neighbors.append(other)
        else:
            print(f'Duplicate neighbor {other} found, not adding to neighbors of {self}')
    
    def remove_neighbor(self, other:'Graph_Node'):
        """Removes a neighbor from the node, as if the graph were undirected."""
        if other in self.neighbors:
            self.neighbors.remove(other)
        else:
            raise KeyError('Could not find desired node in neighbors list.')

    def __add__(self, other):
        self.add_neighbor(other)
    
    def __str__(self):
        return self.id

class Graph:
    def __init__(self, is_directed:bool=True):
        self.nodes = {}
        self.edges = []
        self.is_directed = is_directed
    
    def add_nodes(self, node_ids: list):
        for id in node_ids:
            node = Graph_Node(id)
            self.nodes[id] = node
    
    def add_edges(self, edges: list):
        """
        Adds the edges given in the list given.
        For an edge (X, Y) in the list, if the graph is specified to be undirected,
        the edge will be added as X --> Y
        """
        for edge in edges:
            left_node = self.nodes[edge[0]]
            right_node = self.nodes[edge[1]]
            if self.is_directed:
                left_node.add_neighbor(right_node)
            else:
                left_node.add_neighbor(right_node)
                right_node.add_neighbor(left_node)
            
            self.edges += edge
    
    # TODO: Docstring and check implementation.
    def remove_edges(self, edges:list):
        for edge in edges:
            if edge[0] not in self.nodes.keys() or edge[1] not in self.nodes.keys():
                continue

            left_node = self.nodes[edge[0]]
            right_node = self.nodes[edge[1]]
            if self.is_directed:
                left_node.remove_neighbor(right_node)
            else:
                left_node.remove_neighbor(right_node)
                right_node.remove_neighbor(left_node)
            
            self.edges += edge
    
    def breadth_first_search(self, start_node_id:str):
        """
        Performs standard BFS algorithm on graph. If there are multiple connected
        components, returns the component that corresponds to the start node.
        """
        if len(self.nodes) < 1:
            return
        
        assert start_node_id in self.nodes.keys()

        print(f'Performing BFS starting with node {start_node_id}...')
        bfs_subgraph_nodes = []
        nodes_to_visit = []
        curr_node = self.nodes[start_node_id]
        print(curr_node)
        bfs_subgraph_nodes.append(curr_node)
        curr_node.visited = True
        nodes_to_visit += curr_node.neighbors

        while len(nodes_to_visit) > 0:
            curr_node = nodes_to_visit.pop(0)
            print(curr_node)
            bfs_subgraph_nodes.append(curr_node)
            curr_node.visited = False
            for neighbor in curr_node.neighbors:
                if not neighbor.visited:
                    nodes_to_visit.append(neighbor)
            
        return bfs_subgraph_nodes

    def unvisit_all_nodes(self):
        for node in self.nodes.values:
            node.visited = False
    
    # TODO: Returns an undirected version of the graph (to use in BFS)
    def as_undirected(self):
        return 0

class BST_Node:
    def __init__(self, value):
        assert type(value) == int
        self.value = value
        self.left = None
        self.right = None
    
    def insert_left(self, value):
        """Insert to left child with value specified"""
        self.left = BST_Node(value)
    
    def insert_right(self, value):
        """Insert to right child with value specified"""
        self.right = BST_Node(value)
    
    def is_leaf(self) -> bool:
        """Determines if node is a leaf node (has no children)"""
        return (not self.left) and (not self.right)

    def __gt__(self, other):
        return self.value > other.value

    def __eq__(self, other):
        return self.value == other.value
    
    def __lt__(self, other):
        return self.value < other.value

    def __str__(self):
        return f'Node Value: {self.value}'


class BST:
    def __init__(self, root=None):
        if root:
            self.root = BST_Node(value=root)
        else:
            self.root = None

    def insert(self, value):
        """Inserts node starting from the root."""
        def insert_helper(value, curr_node:BST_Node=None):
            if not curr_node:
                curr_node = BST_Node(value)
                print('Base Case')
                return
            
            if value < curr_node.value and curr_node.left:
                return insert_helper(value, curr_node.left)
            elif value < curr_node.value and not curr_node.left:
                curr_node.insert_left(value)
                print('Inserted Node!')
                return
            elif value > curr_node.value and curr_node.right:
                return insert_helper(value, curr_node.right)
            elif value > curr_node.value and not curr_node.right:
                curr_node.insert_right(value)
                print('Inserted Node!')
                return
            else:
                print('Duplicate node values found.')
                return
        
        insert_helper(value, curr_node=self.root)
        
    
    def inorder_traversal(self, curr_node:BST_Node=None):
        if curr_node is None:
            return 
        
        self.inorder_traversal(curr_node.left)
        print(curr_node)
        self.inorder_traversal(curr_node.right)

def binary_search(nums: list[int], target: int, min_idx: int=None, max_idx: int=None):
    """
    Input list should be sorted. Returns the index of the value desired. 
    If the target value does not exist, returns None.
    """
    if min_idx is None: min_idx = 0
    if max_idx is None: max_idx = len(nums) - 1
    while min_idx <= max_idx:
        mid_idx = min_idx + (max_idx - min_idx) // 2

        if nums[mid_idx] == target: 
            return mid_idx
        elif nums[mid_idx] < target:
            min_idx = mid_idx + 1
        else:
            max_idx = mid_idx - 1
        
    return None

    

if __name__ == '__main__':
    node1 = BST_Node(3)
    node2 = BST_Node(7)
    node1.insert_left(4)

    print(node1)
    print(node1 < node2)
    print(node1 == node2)
    print(node1.is_leaf())

    bst = BST(4)
    bst.insert(3)
    bst.insert(5)
    bst.insert(1)
    bst.insert(1)
    # print(bst.root.left)
    # print(bst.root.right)
    print(bst.inorder_traversal(curr_node=bst.root))

    # Graph tests
    print('\n === GRAPH TESTING === \n')
    graph = Graph(is_directed=True)
    graph.add_nodes(['A', 'B', 'C', 'D', 'E', 'F'])
    graph.add_edges([('A', 'B'), ('A', 'C'), ('A', 'D'), ('E', 'F'), ('C', 'A')])

    graph.breadth_first_search('C')
    graph.breadth_first_search('F')
    graph.breadth_first_search('E')

    print('=== BINARY SEARCH TESTING ===')
    nums_list = [-39,-18,-5,-3,-1,0,1,2,3,5,16,21,28]
    nums_list_2 = sorted(np.random.randint(low=-500, high=500, size=100))
    
    target_idx = binary_search(nums_list, target=30)
    assert target_idx == None

