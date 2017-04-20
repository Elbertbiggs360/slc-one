class BinarySearch(list):
    """Binary Search Class"""

    def __init__(self, a, b):
        super(BinarySearch, self).__init__()
        if isinstance(a, int) and isinstance(b, int):
            for i in range(1, a+1):
                self.append(i*b)
            self.length = len(self)
        else:
            raise TypeError

    def search(self, value):
        found, index = False, 0
        first, counter, last = 0, 0, len(self)-1 #assign first and last places in the generated list as well as initialize counter to 0

        if value == self[first]: #if value is in first position
            found, index = True, 0

        elif value == self[last]: #if value is in last position
            found, index = True, last

        if value > self[last] or value < self[first]: #check if value to search is greater than the largest item in the list or smaller than the smallest item in the list
            found, index =  True, -1

        while first <= last and not found:
            mid = (first + last) //2

            if self[mid] == value:
                found, index = True, mid

            else:
                counter += 1
                if value < self[mid]:
                    last = mid - 1
                else:
                    first = mid + 1

        return {'count': counter, 'index': index}