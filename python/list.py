
class ListItem:
    def __init__(self, value, _next=None):
        self.value = value
        self.next = _next


class List:
    """A List implementatinon not using Python Lists"""

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

    def append(self, value):
        """Appends an item at the end of the List"""
        if self.root is None:
            self.root = ListItem(value, None)
        else:
            it = self.root
            while it.next is not None:
                it = it.next

            it.next = ListItem(value,None)

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

            
if __name__ == '__main__':
    print('List example')

    li = List()
    print('empty list is', li)

    li.prepend(1)
    print('one item', li)

    li.prepend(2)
    print('two items', li)

    li.prepend(3)
    print('three items', li)

    li.append(2)
    print('append 2', li)

    li.append(3)
    print('append 3', li)

    li2 = List()    
    li2.append(1)
    li2.append(2)
    li2.append(3)

    print('new appended list', li2)            

    print('length 1 =', len(li))
    print('length 2 =', len(li2))
    print('length empty =', len(List()))
    print('length init1 =', len(List(5)))

    print('at 2 =', li.at(2))
