from collections import OrderedDict

def partition(iterable,*conditions):
    '''Returns a list with the elements that satisfy each of condition.
       Conditions are assumed to be exclusive'''
    d= OrderedDict((i,list())for i in range(len(conditions)))        
    for e in iterable:
        for i,condition in enumerate(conditions):
            if condition(e):
                d[i].append(e)
                break                    
    return d.values()
