kitten = open("test0.in", "r+")
_dict = {}
def process_line(line, _dict):
    arr = line.replace("\n", "").split(" ")
    if arr[0] != '-1':
        if int(arr[0]) not in _dict:
            _dict[int(arr[0])] = list(map(int, arr[1:]))
        else:
            _dict[int(arr[0])] = _dict[int(arr[0])] + list(map(int, arr[1:]))
    return _dict

first_line = kitten.readline()
# calling out kitten as 0
_dict[int(first_line.replace("\n", ""))] = [0]
for line in kitten:
    _dict = process_line(line, _dict)
print(_dict)
