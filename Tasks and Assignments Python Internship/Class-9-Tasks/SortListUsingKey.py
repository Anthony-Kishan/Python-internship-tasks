# Sort a multiple datatype 2D list using specific sort key. i.e. SORT_KEY = 1

ls = [
    ['a', 'b', 40, 'x'],
    ['c', 'd', 60, 'y'],
    ['e', 'f', 30, 'z']
]

SORT_KEY = 2

def get_index(item):
    '''Function to extract the element using the SORT_KEY index''' 
    x = item[SORT_KEY]
    return x

ls_sorted = sorted(ls, key=get_index)
print(ls_sorted)   

