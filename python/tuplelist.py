
def twobytwo(t):
    """Iterator over a tuple returning two values each interation (or value and ())"""
    tlen = len(t)
    index = 0
    while index < tlen:
        if index != tlen-1:
            yield(t[index], t[index + 1])
        else:
            yield(t[index], ())
            raise StopIteration

        index = index + 2


def merge_tuples(a, b):
    """Merges two sorted tuples onto a sorted tuple"""
    alen = len(a)
    blen = len(b)

    aindex = 0
    bindex = 0

    result = ()

    while aindex < alen and bindex < blen:
        if a[aindex] <= b[bindex]:
            result = result + (a[aindex],)
            aindex = aindex + 1
        else:
            result = result + (b[bindex],)
            bindex = bindex + 1

    if aindex < alen:
        result = result + a[aindex:]
    elif bindex < blen:
        result = result + b[bindex:]

    return result


class TupleList:
    """A List implementation using a tuple as container."""

    def __init__(self, *items):
        """Creates a list with optional initial elements"""
        self.root = items

    def __str__(self):
        """Renders the list as String"""
        return 'TupleList' + self.root.__str__()
        
    def __len__(self):
        """Counts the number of items on the List""" 
        return len(self.root)

    def __getitem__(self, item):
        """Basic __getitem__ for indexed access"""
        if type(item) is slice:
            raise TypeError

        return self.root[item]

    def prepend(self, value):
        """Prepends an item at the beginning of the List"""
        self.root = (value,) + self.root
        return self

    def append(self, value):
        """Appends an item at the end of the List"""
        self.root = self.root + (value,)
        return self

    def at(self, index):
        """Returns the item at the specified index of the List"""
        return self.root[index]

    def delete(self, index, count=1):
        """Deletes count item from index"""
        # in fact, it is not needed to compare...
        if index == 0:
            self.root = self.root[count:]
        else:
            self.root = self.root[:index] + self.root[index+count:]

        return self

    def remove(self, value):
        """Removes first item matching value"""
        for index, v in enumerate(self.root):
            if v == value:
                self.delete(index)
                break

        return self

    def remove_all(self, value):
        """Removes all items matching value"""
        index = len(self.root) - 1
        while index >= 0:
            if self.root[index] == value:
                self.delete(index)

            index = index - 1

        return self

    def set(self, index, value):
        """Sets element at index to value (if it exists)"""
        self.root = self.root[:index] + (value,) + self.root[index+1:]

        return self

    def insert(self, index, value):
        """Inserts value at specified index"""
        self.root = self.root[:index] + (value,) + self.root[index:]

        return self

    def reverse(self):
        """Returns a new list with the result of reversing this list"""
        r = ()

        for value in self.root:
            r = (value,) + r

        return TupleList(*r)

    def clear(self):
        """Clears the contents of the list"""
        self.root = ()
        return self

    def copy(self):
        """Returns a copy of the list"""
        return TupleList(*self.root)

    def insert_sorted(self, value):
        """Inserts value on the list keeping its order"""
        for index, v in enumerate(self.root):
            if value <= v:
                self.root = self.root[:index] + (value,) + self.root[index:]
                return self

        self.root = self.root + (value,)
        return self

    def sort_insert(self):
        """Sorts the list"""
        if len(self.root) <= 1:
            return self

        new_list = TupleList()
        for v in self.root:
            new_list.insert_sorted(v)
        
        self.root = new_list.root
        return self

    def sort_bubble(self):
        if len(self.root) <= 1:
            return self

        swapped = True
        while swapped:
            swapped = False
            for index, value in enumerate(self.root[1:]):
                if value < self.root[index]:
                    swapped = True
                    self.root = self.root[:index] + (value, self.root[index]) + self.root[index+2:]

        return self

    def sort_merge(self):
        if len(self.root) <= 1:
            return self

        # lol = list of lists
        lol = TupleList()

        # step 1: sort elements by pair
        # I'm reusing the Nodes
        for a, b in twobytwo(self.root):
            if b is not ():
                if a <= b:
                    lol.prepend((a, b))
                else:
                    lol.prepend((b, a))

            else:
                lol.prepend((a,))

        # Step 2: merge sublists two by two
        # also reusing the Nodes
        while len(lol.root) > 1:
            old_root = lol.root
            lol.root = ()
            for a, b in twobytwo(old_root):
                lol.prepend(merge_tuples(a, b))

        self.root = lol.root[0]
        return self


if __name__ == '__main__':
    print('LinkedList example')

    print("new empty", TupleList())
    print("new one element", TupleList(1))
    print("new multiple elements", TupleList(1, 2, 3, 4, 5))

    print("len empty", len(TupleList()))
    print("len one element", len(TupleList(1)))
    print("len multiple elements", len(TupleList(1, 2, 3, 4, 5)))

    li = TupleList()
    print('li =', li)
    print('li.prepend(1) =', li.prepend(1))
    print('li.prepend(2) =', li.prepend(2))
    print('li.prepend(3) =', li.prepend(3))
    print('li.append(2) =', li.append(2))
    print('li.append(3) =', li.append(3))
    print('li.at(2) =', li.at(2))
    try:
        print('li.at(8) =', li.at(8))
    except IndexError:
        print("Expected error happened")

    print('li.copy().delete(1,3) =', li.copy().delete(1, 3))
    print('li.delete(2) =', li.delete(2))
    print('li.remove(2) =', li.remove(2))
    print('li.remove_all(3) =', li.remove_all(3))

    li2 = TupleList('a', 'b', 'c', 'd')
    print('li2 =', li2)
    print('li2.set(0,"xxx") =', li2.set(0, "xxx"))
    print('li2.set(8,"out") =', li2.set(8, "out"))
    print('li2.set(3,"zzz") =', li2.set(3, "zzz"))
    print('li2.set(2,"okk") =', li2.set(2, "okk"))
    print('li2.insert(2,"middle") =', li2.insert(2, "middle"))
    print('li2.insert(0,"start") =', li2.insert(0, "start"))
    print('li2.insert(8,"end") =', li2.insert(8, "end"))

    print('reverse 1,2,3 =', TupleList(1, 2, 3).reverse())

    print('li2[2] = ', li2[2])

    insort = TupleList()
    print(insort.insert_sorted(2))
    print(insort.insert_sorted(5))
    print(insort.insert_sorted(4))
    print(insort.insert_sorted(1))
    print(insort.insert_sorted(6))
    print(insort.insert_sorted(3))

    print('insort =', insort)
    print('sort_insert =', TupleList(3, 6, 4, 7, 1, 2, 5, 0).sort_insert())
    print('sort_bubble =', TupleList(3, 6, 4, 7, 1, 2, 5, 0).sort_bubble())
    print('sort_merge  =', TupleList(6, 3, 4, 2, 1, 5, 0).sort_merge())
