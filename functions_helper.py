# get data by address
def get_by_path(data, path):
    current_path = data
    for i in range(len(path)):
        current_path = current_path[path[i]]
    return current_path

# set element to data by address
def set_to_path(data, array, element):
    current_path = data
    for i in range(len(array)-1):
        current_path = current_path[array[i]]
    current_path[array[-1]] = element

# get arguments in binary operation
def binary_type(current, text):
    left = current['left']
    right = current['right']
    if left['type'] == "pointer":
        left = get_by_path(text, left['path'])
        right = get_by_path(text, right['path'])
        return left, right

# get next instruction by address
def get_next(data, path):
    current_path = data
    for i in range(len(path)-1):
        current_path = current_path[path[i]]
    if len(current_path) <= path[-1]:
        return "end"
    else:
        return current_path[path[-1]]

# push element to the stack
def stack_push(text, element):
    text['stack']['array'].insert(0, element)

# get current frame in the stack
def get_current_frame(stack):
    if (len(stack['array']) > stack['active']):
        return stack['array'][stack['active']]
    else:
        return {}

# get result path in current structure
def get_result_path(current, stack):
    if "result_path" in current:
        return current['result_path']
    else:
        return get_current_frame(stack)['result_path']