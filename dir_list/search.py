

# print('I imported module search.py')

def find_Index(to_search,target):
    for x,value in enumerate(to_search):
        if value == target:
            return x
    return f'{target} does not belong to the list'

