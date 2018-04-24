
def reverse(t):
    if t is ():
        return ()

    value, it = t
    result = (value, ())
    while it is not ():
        value, it = it
        result = (value, result)

    return result
    

class LinkedTupleList:
    """A List implementation using linked tuples"""

    def __init__(self, *items):
        """Creates a list with optional initial elements"""
        self.root = ()
        it = self.root
        for value in items:
            if it is ():
                it = (value,())
                self.root = it
            else:
                it = (value,it)

    def __str__(self):
        """Renders the list as String"""
        result = 'LinkedTupleList('
        it = self.root
        sep = ''

        while it is not ():
            value, it = it
            result = result + sep + str(value)
            sep = ', '

        return result + ')'

    def __len__(self):
        """Counts the number of items on the List"""
        count = 0
        it = self.root
        
        while it is not ():
            count = count + 1
            it = it[1]
        
        return count

    def prepend(self, value):
        """Prepends an item at the beginning of the List"""
        self.root = (value, self.root)
        return self

    def append(self, value):
        """Appends an item at the end of the List"""
        if self.root is ():
            self.root = (value, ())
        else:
            v, it = self.root
            newRoot = (v, ())
            while it is not ():
                v, it = it
                newRoot = (v, newRoot)

            self.root = reverse(newRoot)
            
        return self

    def at(self, index):
        """Returns the item at the specified index of the List"""
        if self.root is ():
            return None
        
        offset = 0
        value, it = self.root
        while offset < index and it is not ():
            offset = offset + 1
            value, it = it

        if offset == index:
            return value

        return None


if __name__ == '__main__':
    print('LinkedTupleList example')

    print("new empty", LinkedTupleList())
    print("new one element", LinkedTupleList(1))
    print("new multiple elements", LinkedTupleList(1, 2, 3, 4, 5))

    print("len empty", len(LinkedTupleList()))
    print("len one element", len(LinkedTupleList(1)))
    print("len multiple elements", len(LinkedTupleList(1, 2, 3, 4, 5)))

    li = LinkedTupleList()
    print('li =', li)
    print('li.prepend(1) =', li.prepend(1))
    print('li.prepend(2) =', li.prepend(2))
    print('li.prepend(3) =', li.prepend(3))
    print('li.append(2) =', li.append(2))
    print('li.append(3) =', li.append(3))
    print('li.at(2) =', li.at(2))
    print('li.at(8) =', li.at(8))

    