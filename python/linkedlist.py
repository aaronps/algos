
class ListItem:
    def __init__(self, value, _next=None):
        self.value = value
        self.next = _next


class LinkedList:
    """A List implementation using linked nodes"""

    def __init__(self, first_value=None):
        """Creates a list with optional first element inserted"""
        if first_value is not None:
            self.root = ListItem(first_value)
        else:
            self.root = None

    def __str__(self):
        """Renders the list as String"""
        result = '('
        it = self.root
        sep = ''

        while it is not None:
            result = result + sep + str(it.value)
            sep = ','
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
        self.root = ListItem(value, self.root)
        return self

    def append(self, value):
        """Appends an item at the end of the List"""
        if self.root is None:
            self.root = ListItem(value, None)
        else:
            it = self.root
            while it.next is not None:
                it = it.next

            it.next = ListItem(value,None)

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

    def removeAll(self, value):
        """Removes all items matching value"""
        while self.root is not None and self.root.value == value:
            self.root = self.root.next

        if self.root is not None:
            it = self.root
            while it.next is not None:
                if it.next.value == value:
                    it.next = it.next.next
                            
        return self

    def setAt(self, index, value):
        """Sets element at index to value (if it exists)"""
        it = self.root
        while it is not None and index > 0:
            index = index - 1
            it = it.next

        if it is not None:
            it.value = value

        return self
            
if __name__ == '__main__':
    print('LinkedList example')

    li = LinkedList()
    print('empty list is', li)

    print('one item', li.prepend(1))
    print('two items', li.prepend(2))
    print('three items', li.prepend(3))
    print('append 2', li.append(2))
    print('append 3', li.append(3))

    li2 = LinkedList()    
    li2.append(1)
    li2.append(2)
    li2.append(3)
    print('new appended list', li2)            

    print('length 1 =', len(li))
    print('length 2 =', len(li2))
    print('length empty =', len(LinkedList()))
    print('length init1 =', len(LinkedList(5)), 'List(5)', LinkedList(5))

    print('at 2 =', li.at(2))
    print('setAt(0,5)', li2.setAt(0,5))

    print('delete(2) =', li.delete(2))
    print('remove 2 =', li.remove(2))
    print('removeAll(3) =', li.removeAll(3))
    