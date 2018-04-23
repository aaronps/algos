
class ListItem:
    def __init__(self, value, _next = None):
        self.value = value
        self._next = _next

class List:

    def __init__(self, firstValue = None):
        if firstValue != None:
            self.root = ListItem(firstValue)
        else:
            self.root = None

    def __str__(self):
        result = '('
        it = self.root
        sep = ''
        while it != None:
            result = result + sep + str(it.value)
            sep = ','
            it = it._next

        return result + ')'

    def __len__(self):
        count = 0
        it = self.root
        
        while it != None:
            count = count + 1
            it = it._next
         
        return count
    
    def prepend(self, value):
        self.root = ListItem(value, self.root)             

    def append(self, value):
        if self.root == None:
            self.root = ListItem(value, None)
        else:
            it = self.root
            while it._next != None:
                it = it._next

            it._next = ListItem(value,None)

    def at(self, index):
        if self.root == None:
            return None
        
        offset = 0
        it = self.root
        while offset < index and it != None:
            offset = offset + 1
            it = it._next

        if it != None:
            return it.value

        return None
            
            
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



    