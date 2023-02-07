from collections import ChainMap, Counter, namedtuple, deque

def do_chainmap():
    # Chainmap - linking objects, faster than dictionary or update(calls)

    dict1 = {'x':1, 'y':2,'z':3,'a':4,'b':5}
    dict2 = {1:'a', 2:'b'}
    my_map = list(ChainMap(dict1, dict2))

    dict3 = {1:222, 2:333, 3:444}
    dict4 = {1: 555, 2: 666, 3: 777}
    c = ChainMap(dict3)
    d = c.new_child(dict4) # contains dict3 from parent
    mapped_second_dict_in_d = d.maps[1]
    c['val'] = 2 # set value for 'val' in context c
    del c[3] # removed 3:444 from dict3

def do_some_counting():
    cnt = Counter('abc!')
    cnt2 = Counter({'a': 2, 'b': 3, 'c': 2})
    elems = sorted(cnt2.elements())
    mst_common = cnt2.most_common(1)  # first most common elem
    cnt.subtract(cnt2)  # subtract cnt2 from cnt
    total = cnt2.total()

    a = Counter(a=1, b=2, c=3)
    b = Counter(a=0, b=1, c=3)
    subtr = a - b  # math operations are possible with counter objects
    union_max = a | b
    c = Counter(a=-2, b=1, c=0)
    removed_zero_and_negative = +c
    c.update(a=2, c=-2, d=8)

def do_named_tuple():
    '''named tuples for data assigning'''
    Cat = namedtuple('Cat', 'size sex color')
    my_cat = Cat(13, 'male', 'black')
    size, sex, color = my_cat  # unpacking

    vector = namedtuple('Vector', ['pointX', 'pointY'])
    v1 = vector(5, 5)
    summing = v1[0] + v1[1]  # indexable, can perform math
    subtract = v1.pointX - v1.pointY  # access by names
    v1  # readable __repr__

    dictionary_from_tuple = v1._asdict()
    v1._replace(pointX=6)  # can replace specific fields
    v1._fields  # view field names

    # unpacking dict to named tuple
    my_dict = {'pointX': 179, 'pointY': 83}
    b = vector(**my_dict)


def do_deque():
    d = deque('my string')
    d.append('right side')
    d.appendleft('left side')

    #remove rightmost and leftmost values
    d.pop()
    d.popleft()

    # list contents
    my_deque_list = list(d)
    d_copy = d.copy()
    d.clear()
    counted = d.count(None)
    counted_copy = d_copy.count('g')
    d.append(1)
    d.extend([3])
    d.extendleft([0])
    d.insert(2, 2)  # insert 2 in position 2
    d.remove(0)
    d.reverse()  # reversed deque 3-2-1
    d.reverse()  # reversed deqie 1-2-3
    d.rotate(1)  # deque rotates to 3-1-2, last to first


if __name__ == '__main__':
    do_chainmap()
    do_some_counting()
    do_named_tuple()
    do_deque()