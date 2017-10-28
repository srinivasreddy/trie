class Node(object):
    def __init__(self, char, length=0):
        self.char = char
        self.length = length
        self.next = {}

    def __repr__(self):
        return "Node({}, {}, length:{})".format(self.char, self.next, self.length)

class Trie(object):
    def __init__(self):
        self.root = Node(None)
    
    def insert(self, string):
        next_nodes = self.root.next
        index = 0
        while(index<len(string)):
            _char = string[index]
            if _char in next_nodes:
                target_node = next_nodes[_char]
                if index == 0 and len(string) > target_node.length:
                    target_node.length = len(string)
                next_nodes = target_node.next         
   	    else:
                if index == 0:
                    node = Node(_char, len(string))
                else:
                    node = Node(_char)
                next_nodes[_char] = node
                next_nodes = node.next
            index = index + 1

    def find_max_length_prefix(self, prefix):
        first_char = prefix[0]
        next_nodes = self.root.next
        for _char in prefix:
            if _char in next_nodes:
                next_nodes = next_nodes[_char].next
            else:
                return -1
        return self.root.next[first_char].length
    

if __name__ == "__main__":
    trie = Trie()
    trie.insert("asdas")
    trie.insert("asdasddasdasdasdasdasdas")
    trie.insert("a")
    trie.insert("bsdasd")
    trie.insert("qweqw")
    print trie.find_max_length_prefix("a")
    
