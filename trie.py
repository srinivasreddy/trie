class Node(object):
    def __init__(self, char, value):
        self.char = char
        self.value = value
        self.prefix_max_length=0
        self.next = {}

    def __repr__(self):
        return "Node({}, {}, {}, length:{})".format(self.char, self.value, self.next, self.prefix_max_length)

class Trie(object):
    def __init__(self):
        self.root = Node(None,None)
    
    def insert(self, string, value):
        next_pointers = self.root.next
        index = 0
        while(index<len(string)):
            _char = string[index]
            if _char in next_pointers:
                next_pointers = next_pointers[_char].next                
   	    else:
                if index + 1 == len(string):
                    node = Node(_char, value)
                else:
                    node = Node(_char, None)
                next_pointers[_char] = node
                next_pointers = node.next
            index = index + 1

trie = Trie()
"""
times, input_strings = map(int, raw_input().split())
for _ in range(times):
    char, value = raw_input().split()
    trie.insert(char, int(value))
"""
trie.insert('hackerrank', 9)
trie.insert('hackerrank', 9)
trie.insert('hackerrank', 9)
print trie.suggestions('hacker')
"""
for _ in range(input_strings):
    data = raw_input()
    trie.suggestions(data)
    
"""
