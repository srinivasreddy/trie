
class Node(object):
    def __init__(self, char, value):
        self.char = char
        self.value = value 
        self.next = []
        
class Trie(object):
    def __init__(self):
        self.root = Node(None,None)
    
    def insert(self,root, string, value):
        
        if string =='':  ## base case
            root.value = value
            return
        
        if root is None:
            next_pointers = self.root.next
        else:
            next_pointers = root.next  
        for index, c in enumerate(string):
            found = False
            for  node in next_pointers:
                 if c == node.char:
                     found = True
                     self.insert(node, string[index+1:], value)
                      
            if not found:
                if len(string) == 1:
                    node = Node(c, value)
                else:
                    node = Node(c, None)
                next_pointers.append(node)
                next_pointers = node.next
    
    def _get_highest_suggestion(self, current_node):
        for  node  in current_node.next_pointers:
            if node.value is None:
                continue
            else:
                return max (node.value, self._get_highest_suggestion(node))
        return -1

    def get_next_suggestion(self, string):
        current_node = self.root
        for index, char in enumerate(string):
            found = False
            for node in current_node.next:
                if node.char == char:
                    found = True
                    current_node = node
                    break
            if found:
                return _get_highest_suggestion(current_node)
        return -1
            
    def check(self, string):
        current_node = self.root
        for index, char in enumerate(string):
            for node in current_node.next_pointers:
                if node.char == char:
                    current_node = node
                    continue
            if index+1 == len(string):
                return True
            return False
        return False
    
    def suggestions(self, string):
        if not self.check(string):
            return -1
        print self.get_next_suggestion(string)
        
        
    
        
'''
# Read input from stdin and provide input before running code

name = raw_input()
print 'Hi, %s.' % name
'''
trie = Trie()
import pdb;pdb.set_trace()
times, input_strings = map(int, raw_input().split())
for _ in range(times):
    char, value = raw_input().split()
    trie.insert(None, char, int(value))
for _ in input_strings:
    data = raw_input()
    trie.suggestions(data)
    
