import sys

_dict = {}
global __course
__course = []

def process_line(line, _dict):
    arr = line.replace("\n", "").split(" ")
    if arr[0] != '-1':
        _val = int(arr[0])
        if _val not in _dict:
            _dict[_val] = list(map(int, arr[1:]))
        else:
            _dict[_val] = _dict[_val] + list(map(int, arr[1:]))
    return _dict

def find_course(elem, graph, course):
    if elem == 0:
        global __course
        __course = course
    new_course = course + [elem]
    if elem in graph:
        for graph_elem in graph[elem]:
            find_course(graph_elem, graph, new_course)

kitten = sys.stdin
first_line = kitten.readline()
# calling out kitten as 0
_dict[int(first_line.replace("\n", ""))] = [0]
one_before = int(first_line.replace("\n", ""))
for line in kitten:
    _dict = process_line(line, _dict)

# find root
_maxx = 0
check = {}
arr = set()
for key in _dict.keys():
    _maxx = max(key, _maxx)
    arr.add(key)
    for val in _dict[key]:
        arr.add(val)
        _maxx = max(val, _maxx)
        check[val] = True
root_val = 0
for x in arr:
    if x not in check:
        root_val = x
        break

# begin breadth first search from root
find_course(root_val, _dict, [root_val])
__course.reverse()
print(' '.join((str(e) for e in __course[:-1])))

