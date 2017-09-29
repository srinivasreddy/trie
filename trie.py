
class Node(object):
    def __init__(self, char, value):
        self.char = char
        self.value = value 
        self.next = {}

    def __repr__(self):
        return "Node({},{},{})".format(self.char, self.value, self.next)

class Trie(object):
    def __init__(self):
        self.root = Node(None,None)
    
    def insert(self, string, value):
        next_pointers = self.root.next
        index = 0
        while(index<len(string)):
            if string[index] in next_pointers:
                next_pointers = next_pointers[string[index]].next
   	    else:
               	if len(string) == 1 or index + 1 == len(string):
                    node = Node(string[index], value)
                else:
                    node = Node(string[index], None)
                    next_pointers[string[index]] = node
                    next_pointers = node.next
            index = index + 1
    
    def _get_highest_suggestion(self, current_node):
        for  node  in current_node.next:
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
                return self._get_highest_suggestion(current_node)
        return -1
            
    def check(self, string):
        current_node = self.root
        for index, char in enumerate(string):
            for node in current_node.next:
                if node.char == char:
                    current_node = node
                    continue
            if index+1 == len(string):
                return True
            return False
        return False
    
    def suggestions(self, string):
        #if not self.check(string):
        #    return -1
        print self.get_next_suggestion(string)
        
        
    
        
'''
# Read input from stdin and provide input before running code

name = raw_input()
print 'Hi, %s.' % name
'''
trie = Trie()
import pdb;pdb.set_trace()
#times, input_strings = map(int, raw_input().split())
#for _ in range(times):
 #   char, value = raw_input().split()
trie.insert('hackerearth', 10)
trie.insert('hackerrank', 9)
trie.suggestions('hacker')
#for _ in input_strings:
#   data = raw_input()
#    trie.suggestions(data)
    
