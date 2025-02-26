class graph:
	def __init__(self,num_vertices):
		self.num_vertices=num_vertices
		seld.adj_list={}
		for i in range(num_vertices):
			self.adj_list[i]=[]

	def add_edge(self,node1,node2):
		self.adj_list[node1].append(node2) #at node1 edge node2 value will get appended
		self.adj_list[node2].append(node1)

	def dfs(self, start_node,visited):
		print(start_node,end=" ")
		visited[start_node]=True #once visited mark it as true , initially false
		for neighbour in self.adj_list[start_node]:
			if not visited[neighbour]:
				self.dfs(neighbour,visited)


num_vertices,num_edges=map(int,input().split())



