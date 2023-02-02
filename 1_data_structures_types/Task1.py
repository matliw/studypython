from collections import namedtuple
from typing import NamedTuple

my_string = 'my_Test_string Test aaa 123 Test'


def do_stuff_with_strings(txt): # immutable
    string_startpoint = txt.find('Test', 10, 20)
    occurences = txt.count('Test')
    repl = txt.replace('Test', 'Tested')
    lowfi = txt.find('Test')
    highfi = txt.rfind('Test')
    string_list_separated_by_space = txt.rsplit()
    zxczxc = 1
    return None




def do_stuff_with_lists(txt): # mutable
    a_list = [x for x in txt]
    a_list.append(7) # add to the end of list
    a_list.pop() # remove last 7
    b_list = my_string.rsplit() # Split into listed, space separated items
    b_list.remove('Test') # remove first occurence
    sliceA = a_list[1:4:2] # slice from 0-3 every second step

    *c_list, = 1,2,3,4 # pack list
    one,two,*other = c_list # unpack one, two | pack other elements into a list
    unpack_one = one
    unpack_other = other

    index = a_list.index()

    return None
    
def do_stuff_with_tuples(txt): # immutable
    my_tuple = tuple(i for i in txt)
    tuple_slice = my_tuple[0:3]
    tuple_index_1 = tuple_slice[0]
    tuples_index_2 = tuple_slice[1] # tuple contents accessible by index integer
    # tuple[1] = 'w' # can't assign tuples // also no protection from assigning incorrect order on creation as in dictionary
    my_tuple + (55,) # tuples cannot be changed, see below
    assert my_tuple == tuple(i for i in txt)

    '''named tuples for data assigning'''
    Cat = namedtuple('Cat', 'size sex color')
    my_cat = Cat(13, 'male', 'black')

    '''named tuple with type hint support'''
    class Cat_tuple(NamedTuple):
        size: int
        sex: str
        color: str

    cat2 = Cat_tuple(16, 'female', 'white')
    my_cat_color = cat2.color

def do_arrays(): # mutable
    import array
    my_arr = array.array('f', (1.2, 2.0, 4.0)) # arrays are typed: 'f' -> floating point
    my_arr[0] = 1.5 # change array
    del my_arr[0]
    my_arr.append(15.0)

def do_bytes():
    my_arr = bytes((1,2,3,4)) # immutable, range 0-255
    my_arr[0]
    try:
        my_arr[0] = 2
    except TypeError:
        print('Error! I\'m immutable')

    '''bytearray is similar but mutable, 0-255 values'''
    my_arr = bytearray((1,2,4,3))
    my_arr[0]
    my_arr[0] = 4
    my_arr[0]
    del my_arr[0]
    my_arr.append(77)
    try:
        my_arr[2] = 'string'
    except TypeError:
        print('I can only hold bytes!')


    zxczxczxc

def do_stuff_with_sets(txt):
    pass
def do_stuff_with_dictionary(txt):
    listofchars = [x for x in txt]
    my_dict = {x : listofchars[x] for x in range(0, len(txt))} # add index position as a key for each value in the list and convert to dict as key:value pairs
    keys = ['R','G','B']
    values = ['red', 'green', 'blue']
    zipped_dict = dict(zip(keys, values))
    assert zipped_dict['R'] == 'red'


if __name__ == "__main__":
    do_stuff_with_strings(my_string)
    do_stuff_with_lists(my_string)
    do_stuff_with_tuples(my_string)
    do_stuff_with_dictionary(my_string)
    do_arrays()
    do_bytes()