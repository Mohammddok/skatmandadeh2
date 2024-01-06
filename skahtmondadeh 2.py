class Node: 
    def init(self, data): 
        self.data = data 
        self.next = None 
 
class ConnectedLst: 
    def init(self): 
        self.head = None 
    def insert_at_start(self, data): 
        node_jadid = Node(data) 
        node_jadid.next = self.head 
        self.head = node_jadid 
 
    def display(self): 
        current = self.head 
        while current: 
            print(current.data, end=" ") 
            current = current.next 
        print() 
 
Connected_LST = ConnectedLst() 
 
Connected_LST.insert_at_start(3) 
Connected_LST.insert_at_start(2) 
Connected_LST.insert_at_start(1) 
 
Connected_LST.display()
