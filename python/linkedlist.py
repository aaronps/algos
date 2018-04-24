
class Node:
    def __init__(self, value, next_=None):
        self.value = value
        self.next = next_


class LinkedList:
    """A List implementation using linked nodes"""

    def __init__(self, *items):
        """Creates a list with optional initial elements"""
        self.root = None
        it = self.root
        for value in items:
            if it is None:
                it = Node(value)
                self.root = it
            else:
                it.next = Node(value)
                it = it.next

    def __str__(self):
        """Renders the list as String"""
        result = 'LinkedList('
        it = self.root
        sep = ''

        while it is not None:
            result = result + sep + str(it.value)
            sep = ', '
            it = it.next

        return result + ')'

    def __len__(self):
        """Counts the number of items on the List"""
        count = 0
        it = self.root
        
        while it is not None:
            count = count + 1
            it = it.next
         
        return count

    def prepend(self, value):
        """Prepends an item at the beginning of the List"""
        self.root = Node(value, self.root)
        return self

    def append(self, value):
        """Appends an item at the end of the List"""
        if self.root is None:
            self.root = Node(value, None)
        else:
            it = self.root
            while it.next is not None:
                it = it.next

            it.next = Node(value, None)

        return self

    def at(self, index):
        """Returns the item at the specified index of the List"""
        if self.root is None:
            return None
        
        offset = 0
        it = self.root
        while offset < index and it is not None:
            offset = offset + 1
            it = it.next

        if it is not None:
            return it.value

        return None

    def delete(self, index):
        """Deletes the item at specified index"""
        if index == 0:
            if self.root is not None:
                self.root = self.root.next

        else:
            offset = 1
            it = self.root

            while offset < index and it is not None:
                offset = offset + 1
                it = it.next

            if it is not None and it.next is not None:
                it.next = it.next.next

        return self

    def remove(self, value):
        """Removes first item matching value"""
        if self.root is not None:
            if self.root.value == value:
                self.root = self.root.next
            else:
                it = self.root
                while it.next is not None:
                    if it.next.value == value:
                        it.next = it.next.next
                        break
                        
        return self

    def remove_all(self, value):
        """Removes all items matching value"""
        while self.root is not None and self.root.value == value:
            self.root = self.root.next

        if self.root is not None:
            it = self.root
            while it.next is not None:
                if it.next.value == value:
                    it.next = it.next.next
                            
        return self

    def set(self, index, value):
        """Sets element at index to value (if it exists)"""
        it = self.root
        while it is not None and index > 0:
            index = index - 1
            it = it.next

        if it is not None:
            it.value = value

        return self

    def insert(self, index, value):
        """Inserts value at specified index"""
        if index == 0:
            self.root = Node(value, self.root)
        else:
            it = self.root
            count = 1
            while count < index and it.next is not None:
                count = count + 1
                it = it.next

            it.next = Node(value, it.next)

        return self

    def reverse(self):
        """Returns a new list with the result of reversing this list"""
        new_list = LinkedList()
        
        it = self.root
        while it is not None:
            new_list.prepend(it.value)
            it = it.next
            
        return new_list


if __name__ == '__main__':
    print('LinkedList example')

    print("new empty", LinkedList())
    print("new one element", LinkedList(1))
    print("new multiple elements", LinkedList(1, 2, 3, 4, 5))

    print("len empty", len(LinkedList()))
    print("len one element", len(LinkedList(1)))
    print("len multiple elements", len(LinkedList(1, 2, 3, 4, 5)))

    li = LinkedList()
    print('li =', li)
    print('li.prepend(1) =', li.prepend(1))
    print('li.prepend(2) =', li.prepend(2))
    print('li.prepend(3) =', li.prepend(3))
    print('li.append(2) =', li.append(2))
    print('li.append(3) =', li.append(3))
    print('li.at(2) =', li.at(2))
    print('li.at(8) =', li.at(8))
    print('li.delete(2) =', li.delete(2))
    print('li.remove(2) =', li.remove(2))
    print('li.remove_all(3) =', li.remove_all(3))

    li2 = LinkedList('a', 'b', 'c', 'd')
    print('li2 =', li2)
    print('li2.set(0,"xxx") =', li2.set(0, "xxx"))
    print('li2.set(8,"out") =', li2.set(8, "out"))
    print('li2.set(3,"zzz") =', li2.set(3, "zzz"))
    print('li2.set(2,"okk") =', li2.set(2, "okk"))
    print('li2.insert(2,"middle") =', li2.insert(2, "middle"))
    print('li2.insert(0,"start") =', li2.insert(0, "start"))
    print('li2.insert(8,"end") =', li2.insert(8, "end"))

    print('reverse 1,2,3 =', LinkedList(1, 2, 3).reverse())
