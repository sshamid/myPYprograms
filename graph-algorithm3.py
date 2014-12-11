
# coding: utf-8

# In[5]:


# Adjacency list Graph Implementation

class Graph:

    def __init__(self):
        """Construct Empty Graph"""
        self.edges = {}

    def addVertex(self, v):
        """Add vertex to graph (if not already present)"""
        if v not in self.edges:
            self.edges[v] = []

    def addEdge(self, from_v, to_v):
        """Add edge to graph"""

        if from_v not in self.edges:
            self.edges[from_v] = []
        if to_v not in self.edges:
            self.edges[to_v] = []

        if to_v not in self.edges[from_v]:
            self.edges[from_v].append(to_v)
        if from_v not in self.edges[to_v]:
            self.edges[to_v].append(from_v)


    def isEdge(self, from_v, to_v):
        """Determines whether edge exists"""

        if to_v not in self.edges:
            return False
        if from_v not in self.edges:
            return False

        return to_v in self.edges[from_v]

simple = {1 : [2, 3, 5],
          2 : [1, 4],
          3 : [1],
          4 : [2, 5],
          5 : [1, 4] }

            
def loadGraph (edges):
    """Create a graph instance"""

    g = Graph()
    for v in edges:
        g.addVertex(v)
        for neighbor in edges[v]:
            g.addEdge(v, neighbor)

    return g

g = loadGraph(simple)
g.isEdge(1,5)


# In[5]:

class Graph:
    """ create an empty graph """
    def __init__(self):
        self.edges = {}
    def addVertex(self, v):
        if v not in self.edges:
            self.edges[v] = []
    def addEdges(self, from_v, to_v):
        if from_v not in self.edges:
            self.edges[from_v] = []
        if to_v not in self.edges:
            self.edges[to_v] = []
        
        if to_v not in self.edges[from_v]: 
            self.edges[from_v].append(to_v)
        if from_v not in self.edges[to_v]: 
            self.edges[to_v].append(from_v)
    def isEdge(self, u, v):
        if u not in self.edges:
            return False
        if v not in self.edges:
            return False
        return v in self.edges[u]


class dfsTraversal:
    def __init__(self, graph, s):
        self.graph = graph
        self.start = s
        self.color = {}
        self.pred = {}
        for v in graph.edges:
            self.color[v] = White
            self.pred[v] = None
        self.dfsvisit(s)
    def dfsvisit(self, u):
        self.color[u] = Gray
        for v in self.graph.edges[u]:
            if self.color[v] is White:
                self.pred[v] = u
                self.dfsvisit(v)
        self.color[u] = Black
        
    def solution(self, v):
        if v not in self.graph.edges:
            return None
        if self.pred[v] is None:
            return None
        path = [v]
        while v != self.start:
            v = self.pred[v]
            path.insert(0, v)
        return path

simple = {1 : [2, 3, 5],
          2 : [1, 4],
          3 : [1],
          4 : [2, 5],
          5 : [1, 4] }

def loadGraph(edge):
    g = Graph()
    for u in edge:
        for v in edge[u]:
            g.addEdges(u, v)
    return g

White = 0
Gray  = 1
Black = 2


g = loadGraph(simple)
dfs = dfsTraversal(g, 3)
print dfs.solution(5)


# In[6]:


class Graph:
    """ create an empty graph """
    def __init__(self):
        self.edges = {}
    def addVertex(self, v):
        if v not in self.edges:
            self.edges[v] = []
    def addEdges(self, from_v, to_v):
        if from_v not in self.edges:
            self.edges[from_v] = []
        if to_v not in self.edges:
            self.edges[to_v] = []
        
        if to_v not in self.edges[from_v]: 
            self.edges[from_v].append(to_v)
        if from_v not in self.edges[to_v]: 
            self.edges[to_v].append(from_v)
    def isEdge(self, u, v):
        if u not in self.edges:
            return False
        if v not in self.edges:
            return False
        return v in self.edges[u]


class bfsTraversal:
    def __init__(self, graph, s):
        self.graph = graph
        self.start = s
        self.color = {}
        self.pred = {}
        for v in graph.edges:
            self.color[v] = White
            self.pred[v] = None
        q = Queue()
        q.put(s)

        while (q.qsize()) > 0:
            u = q.get() # get and remove from queue
            for v in self.graph.edges[u]:
                if self.color[v] is White:
                    self.color[v] = Gray
                    self.pred[v] = u
                    q.put(v)
            self.color[u] = Black
        
    def solution(self, u):
        if u not in self.graph.edges:
            return None
        if self.pred[u] is None:
            return None
        path = [u]
        while u != self.start:
            u = self.pred[u]
            path.insert(0, u)
        return path

simple = {1 : [2, 3, 5],
          2 : [1, 4],
          3 : [1],
          4 : [2, 5],
          5 : [1, 4] }

def loadGraph(edge):
    g = Graph()
    for v in edge:
        for u in edge[v]:
            g.addEdges(v, u)
    return g

White = 0
Gray  = 1
Black = 2

from Queue import *
g = loadGraph(simple)
bfs = bfsTraversal(g, 3)
print bfs.solution(5)


# In[ ]:

graph = { 0: {1: 2, 4: 4, 3: 8},
          1: {0:2, 2: 3},
          2: {1: 3, 4: 1, 3: 5},
          3: {2: 5, 4: 7, 0: 8},
          4: {0: 4, 2: 1, 3: 7}
         }

# Note Prim's algorithm needs to know whether PQ contains vertex. This
# operation is not supported (since it won't be efficient). Fortunately
# with O(n) extra storage, this function creates inqueue[] dictionary
# to keep track of the vertices in the PQ.
def computeMST(graph):
    """Return set of edges that forms MST starting search from s"""

    key = {}
    pred = {}
    inqueue = {}
    for v in graph:
        key[v] = sys.maxint
        pred[v] = None

    # choose any vertex to start from. Use last from previous loop
    key[v] = 0
    pq = BHeap(len(graph))
    for v in graph:
        pq.insert(v, key[v])
        inqueue[v] = True

    while not pq.isEmpty():
        u = pq.smallest()
        inqueue[u] = False
        
        for v in graph[u]:
            if inqueue[v]:
                wt = graph[u][v]
                if wt < key[v]:
                    pred[v] = u
                    key[v] = wt
                    pq.decreaseKey(v, wt)

    return pred

def solution(pred):
    """Produce edge list for MST"""
    
    edges = []
    for v in pred:
        if pred[v] is not None:
            edges.append((pred[v], v))

    return edges


# In[23]:

# key are vertices; each edge has weight and that's encoded as well
graph = {0: {1: 2, 4:4},
         1: {2:3},
         2: {3:5, 4:1 },
         3: {0: 8},
         4: {3:3}}

import sys
def allpairshortestpath(g):
    dist = {}
    pred = {}
    for u in g:
        dist[u] = {}
        pred[u] = {}
        for v in g:
            dist[u][v] = sys.maxint
            pred[u][v] = None
        dist[u][u] = 0
        pred[u][u] = None
        for v in g[u]:
            dist[u][v] = g[u][v]
            pred[u][v] = u
    
    for mid in g:
        for u in g:
            for v in g:
                newlen = dist[u][mid] + dist[mid][v]
                if newlen < dist[u][v]:
                    dist[u][v] = newlen
                    pred[u][v] = pred[mid][v]
                    
    return (dist, pred)

allpairshortestpath(graph)

def constructshortestpath(s, t, pred):
    path= [t]
    while s != t:
        t = pred[s][t]
        path.insert(0, t)
    return path

dist, pred = allpairshortestpath(graph)

constructshortestpath(0, 3, pred)


# In[50]:

def buildHeap(A):
    """Construct heap from array A"""
    n = len(A)
    for i in range(n/2-1, -1, -1):
        heapify(A, i, n)

def heapify (A, idx, maxIdx):
    """Ensure structure rooted at A[idx] is a heap"""
    left = 2*idx+1
    right = 2*idx+2
    if left < maxIdx and A[left] > A[idx]:
        largest = left
    else: 
        largest = idx
    if right < maxIdx and A[right] > A[largest]:
        largest = right

    if largest != idx:
        A[idx],A[largest] = A[largest],A[idx]
        heapify(A, largest, maxIdx)

def heapsort(A):
    """Perform heapsort on A"""
    
    buildHeap(A)
    for i in range(len(A)-1, 0, -1):
        A[0],A[i] = A[i],A[0]
        heapify(A, 0, i)
        
graph = { 0: {1: 6, 3: 18, 2: 8},
          1: {4: 11},
          2: {3: 9},
          3: {},
          4: {5: 3},
          5: {3: 4, 2: 7}
         }
x = heapsort(graph)
print x


# In[1]:

# BinaryHeap implementation (with decreaseKey operation)

# Each element is a list of two elements (priority, element)   
PRIORITY = 0
ID = 1

# data structure. Start by describing the priority queue as storing
# identifiers (drawn from set [0, n-1]) and an associated integer priority
# where lower values imply greater importance

class BHeap:

    def __init__(self, size):
        """initialize Binary Heap to given number of elements"""
        self.size      = size
        self.n         = 0
        self.elements  = [[0, None] for i in range(size+1)]
        self.positions = [0 for i in range(size+1)]

    def isEmpty(self):
        """Determine whether Binary Heap is empty"""
        return self.n == 0

    def smallest(self):
        """Extract and return smallest element in heap"""
        id = self.elements[1][ID]
        
        # heap will have one less entry, so place final one appropriately
        last = self.elements[self.n]
        self.n -= 1

        self.elements[1] = last #swapping the last element with root
        pIdx = 1
        child = pIdx * 2
        while child <= self.n:
            # this while loop is equivalent to heapify
            # select smaller of two children
            sm = self.elements[child]
            if child < self.n:
                if sm[PRIORITY] > self.elements[child+1][PRIORITY]:
                    child += 1
                    sm = self.elements[child]

            if last[PRIORITY] <= sm[PRIORITY]:
                break

            self.elements[pIdx] = sm 
            self.positions[sm[ID]] = pIdx

            pIdx = child
            child = 2*pIdx

        self.elements[pIdx] = last
        self.positions[last[ID]] = pIdx
        return id
    

    def insert(self, id, priority):
        """Insert item into heap with given priority"""
        self.n += 1
        i = self.n
        while i > 1:
            pIdx = int(i/2)
            p = self.elements[pIdx]

            if priority > p[PRIORITY]:
                break

            self.elements[i] = p
            self.positions[p[ID]] = i
            i = pIdx

        self.elements[i] = [priority, id]
        self.positions[id] = i
        
    def decreaseKey(self, id, newPriority):
        """Reduce the priority for the given item"""

        size = self.n
        self.n = self.positions[id] - 1 # we will increase self.n when we insert in the next line

        self.insert(id, newPriority)

        self.n = size

#from bheap import BHeap
import sys

# sample graph with edge weights
graph = { 0: {1: 6, 3: 18, 2: 8},
          1: {4: 11},
          2: {3: 9},
          3: {},
          4: {5: 3},
          5: {3: 4, 2: 7}
         }
          
def singleSourceShortestPath(graph, s):
    """Compute and return (dist, pred) matrices of computation"""

    pq = BHeap(len(graph))
    dist = {}
    pred = {}
    
    for v in graph:
        dist[v] = sys.maxint
        pred[v] = None
    dist[s] = 0

    for v in graph:
        pq.insert(v, dist[v])

    while not pq.isEmpty():
        u = pq.smallest()
        for v in graph[u]:
            wt = graph[u][v]
            newLen = dist[u] + wt

            if newLen < dist[v]:
                pq.decreaseKey(v, newLen)
                dist[v] = newLen
                pred[v] = u
                
    return (dist, pred)

def solution(s, v, dist, pred):
    """Return path and total information for shortest path from s to v"""

    path = [v]
    total = dist[v]
    while v != s:
        v = pred[v]
        path.insert(0, v)

    return "length=" + str(total) + " " + str(path)


# In[35]:

graph = { 0: {1: 6, 3: 18, 2: 8},
          1: {4: 11},
          2: {3: 9},
          3: {},
          4: {5: 3},
          5: {3: 4, 2: 7}
         }
dist,pred = singleSourceShortestPath(graph, 1)
dist


# In[2]:

graph = { 0: {1: 2, 4: 4, 3: 8},
          1: {0:2, 2: 3},
          2: {1: 3, 4: 1, 3: 5},
          3: {2: 5, 4: 7, 0: 8},
          4: {0: 4, 2: 1, 3: 7}
         }

# Note Prim's algorithm needs to know whether PQ contains vertex. This
# operation is not supported (since it won't be efficient). Fortunately
# with O(n) extra storage, this function creates inqueue[] dictionary
# to keep track of the vertices in the PQ.
def computeMST(graph):
    """Return set of edges that forms MST starting search from s"""

    key = {}
    pred = {}
    inqueue = {}
    for v in graph:
        key[v] = sys.maxint
        pred[v] = None

    # choose any vertex to start from. Use last from previous loop
    key[v] = 0
    pq = BHeap(len(graph))
    for v in graph:
        pq.insert(v, key[v])
        inqueue[v] = True

    while not pq.isEmpty():
        u = pq.smallest()
        inqueue[u] = False
        
        for v in graph[u]:
            if inqueue[v]:
                wt = graph[u][v]
                if wt < key[v]:
                    pred[v] = u
                    key[v] = wt
                    pq.decreaseKey(v, wt)

    return pred

def solution(pred):
    """Produce edge list for MST"""
    
    edges = []
    for v in pred:
        if pred[v] is not None:
            edges.append((pred[v], v))

    return edges


# In[3]:

pred = computeMST(graph)


# In[4]:

solution(pred)


# In[ ]:



