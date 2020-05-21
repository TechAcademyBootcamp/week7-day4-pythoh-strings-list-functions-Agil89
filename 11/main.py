import random

list1 = input('Enter the first list: ')
list2 = input('Enter the second list: ')

l = []

for x in list1.split(' '):
    l.append(x)
for x in list2.split(' '):
    l.append(x)
def ran(l):
    return random.choice(l)
def minValue(l):
    new_list = set(l)
    new_list.remove(min(new_list))
    return  min(new_list)

def maxValue(l):
    new_list = set(l)
    new_list.remove(max(new_list))
    return max(new_list)