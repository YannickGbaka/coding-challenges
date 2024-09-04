from LinkedList import LinkedList

class Graph:
    def __init__(self, vertices) -> None:
        self.vertices = vertices
        self.lists = []
        
        
        for i in range(vertices):
            self.lists.append(LinkedList())
            
    def add_edge(self, source, destination):
        if (source < self.vertices and destination < self.vertices):
            self.array[source].insert_at_head(destination)
        
    
    def print_graph(self):
        print(">>Adjacency List of Directed Graph<<")
        for i in range(self.vertices):
            print("|", i , end="| => ")
            temp = self.array[i].get_head()
            
            while temp is not None:
                print("[", temp.data, end="] ->")
                temp = temp.next
                
            print("None")

