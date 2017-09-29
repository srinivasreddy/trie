
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
                if index + 1 == len(string):
                    node = Node(string[index], value)
                else:
                    node = Node(string[index], None)
                next_pointers[string[index]] = node
                next_pointers = node.next
            index = index + 1

    def print_max(self, next_pointers):
        max_each = []
        if len(next_pointers) == 0:
            return -1
        for pointer in next_pointers:
            if next_pointers[pointer].value is None and not next_pointers[pointer].next :
                return -1
            else:
                max_each.append(max(next_pointers[pointer].value, self.print_max(next_pointers[pointer].next)))
        return max(max_each)
    
    def suggestions(self, string):
        next_pointers = self.root.next
        index = 0
        while(index<len(string)):
            if string[index] not in next_pointers:
                index = index+1
                break
            else:
                next_pointers = next_pointers[string[index]].next
                index = index+1
        return self.print_max(next_pointers)
        

############## MAIN ###############################

trie = Trie()
times, input_strings = map(int, raw_input().split())
for _ in range(times):
    char, value = raw_input().split()
    trie.insert(char, int(value))
#trie.insert('hackerrank', 9)
#print trie.suggestions('hacker')
for _ in range(input_strings):
    data = raw_input()
    trie.suggestions(data)
    
