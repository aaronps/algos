
def reverse(t):
    """Reverses a linked tuple list's linked tuples."""
    result = ()
    while t is not ():
        value, t = t
        result = value, result

    return result
    

class LinkedTupleList:
    """A List implementation using linked tuples"""

    def __init__(self, *items):
        """Creates a list with optional initial elements"""
        it = ()
        for value in items:
            it = value, it

        self.root = reverse(it)

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

    def __getitem__(self, item):
        """Basic __getitem__ for indexed access"""
        if type(item) is slice:
            raise TypeError

        return self.at(item)

    def prepend(self, value):
        """Prepends an item at the beginning of the List"""
        self.root = value, self.root
        return self

    def append(self, value):
        """Appends an item at the end of the List"""
        self.root = reverse((value, reverse(self.root)))
        return self

    def at(self, index):
        """Returns the item at the specified index of the List"""
        it = self.root
        offset = 0
        while it is not ():
            value, it = it
            if offset == index:
                return value

            offset = offset + 1

        return None

    def delete(self, index, count=1):
        """Deletes count items from index"""
        it = self.root
        result = ()
        offset = 0
        delete_to = index + count
        while it is not ():
            if offset < index or offset >= delete_to:
                result = it[0], result

            it = it[1]
            offset = offset + 1

        self.root = reverse(result)
        return self

    def remove(self, value):
        """Removes first item matching value"""
        it = self.root
        result = ()
        while it is not ():
            if value is not None and it[0] == value:
                value = None
            else:
                result = it[0], result

            it = it[1]

        self.root = reverse(result)
        return self

    def remove_all(self, value):
        """Removes all items matching value"""
        it = self.root
        result = ()
        while it is not ():
            if it[0] != value:
                result = it[0], result

            it = it[1]

        self.root = reverse(result)
        return self

    def set(self, index, value):
        """Sets element at index to value (if it exists)"""
        it = self.root
        result = ()
        count = 0
        while it is not ():
            if count == index:
                result = value, result
            else:
                result = it[0], result

            count = count + 1
            it = it[1]

        self.root = reverse(result)
        return self

    def insert(self, index, value):
        """Inserts value at specified index"""
        it = self.root
        result = ()
        count = 0
        while it is not ():
            if count == index:
                result = value, result

            count = count + 1
            result = it[0], result
            it = it[1]

        if count <= index:
            result = value, result

        self.root = reverse(result)            
        return self

    def reverse(self):
        """Returns a new list with the result of reversing this list"""
        result = LinkedTupleList()
        result.root = reverse(self.root)
        return result

    def clear(self):
        """Clears the contents of the list"""
        self.root = ()
        return self

    def copy(self):
        """Returns a copy of the list"""
        result = LinkedTupleList()
        # we can reuse because tuples are immutable
        result.root = self.root
        return result


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
    print('li.copy().delete(1,3) =', li.copy().delete(1, 3))
    print('li.delete(2) =', li.delete(2))
    print('li.remove(2) =', li.remove(2))
    print('li.remove_all(3) =', li.remove_all(3))

    li2 = LinkedTupleList('a', 'b', 'c', 'd')
    print('li2 =', li2)
    print('li2.set(0,"xxx") =', li2.set(0, "xxx"))
    print('li2.set(8,"out") =', li2.set(8, "out"))
    print('li2.set(3,"zzz") =', li2.set(3, "zzz"))
    print('li2.set(2,"okk") =', li2.set(2, "okk"))
    print('li2.insert(2,"middle") =', li2.insert(2, "middle"))
    print('li2.insert(0,"start") =', li2.insert(0, "start"))
    print('li2.insert(8,"end") =', li2.insert(8, "end"))

    print('reverse 1,2,3 =', LinkedTupleList(1, 2, 3).reverse())

    print('li2[2] = ', li2[2])
