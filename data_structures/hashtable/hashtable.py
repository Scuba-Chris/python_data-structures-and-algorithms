from hashlib import md5
from data_structures.linked_list.linked_list import LinkedList

'''
I watched a couple videos and read some articles on medium.com to help get me through this hashtable
'''

hash_table_size = 32

class HashTable:

    def __init__(self):
        self.bucket = [LinkedList() for i in range(hash_table_size)]
        self.keys = set()

    def hash(self, key):
        k = 0
        for i in list(md5(str(key).encode('utf-8')).hexdigest()):
            k += ord(i)
        return k % len(self.bucket)

    def add(self, key, value):
        if key in self.keys:
            return
        key_hash = self.hash(key)
        self.keys.add(key)
        bucket_ll = self.bucket[key_hash]

        node = None
        current = bucket_ll.head
        while not current == None and node == None:
            if current.value == key:
                node = current
            current = current.next

        if node == None:
            bucket_ll.append({key : value})
        else:
            node.value[key] = value

    def get(self, key):

        bucket_ll = self.bucket[self.hash(key)]

        current = bucket_ll.head
        while current:
            for i in current.value:
                if i == key:
                    return current.value[i]
            current = current.next
        return None

    def contains(self, key):

        bucket_ll = self.bucket[self.hash(key)]

        current = bucket_ll.head
        while current:
            for i in current.value:
                if i == key:
                    return True
            current = current.next
        return False

    def __getitem__(self, index):
        if isinstance(index, str):
            return self.get(index)
        if isinstance(index, int):
            return list(self.keys)[index]
        raise ValueError
                