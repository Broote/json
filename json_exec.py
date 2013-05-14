import json
import pdb
import copy
#pdb.set_trace()
#implemented linear +, -, *, /, &&, ||, >, <, ==, if, input, goto


def get_by_path(data, path):
    current_path = data
    for i in range(len(path)):
        current_path = current_path[path[i]]
    return current_path

def set_to_path(data, array, element):
    current_path = data
    for i in range(len(array)-1):
        current_path = current_path[array[i]]
    current_path[array[-1]] = element

def binary_type(current, text):
    left = current['left']
    right = current['right']
    if left['type'] == "pointer":
        left = get_by_path(text, left['path'])
        right = get_by_path(text, right['path'])
        return left, right

# годится только для поинтеров вида ["program", 0].
# надо переделать на более общий случай
#def get_next(next):
#    if next == "end":
#        return "end"
#    elif next['type'] == "pointer":
#        prog['current_address'] = next['path']
        # возвращается text['program'][number], а если уровень глубже? TODO?
        # подумать, стоит ли каждый раз передавать program
#        return text[next['path'][0]][next['path'][1]]

def get_next(data, path):
    current_path = data
    for i in range(len(path)-1):
        current_path = current_path[path[i]]
    #if (isinstance(path[-1], int) and len(current_path) <= path[-1]):
    if len(current_path) <= path[-1]:
        return "end"
    else:
        return current_path[path[-1]]


def stack_push(element):
    text['stack']['array'].insert(0, element)

def get_current_frame(stack):
    return stack['array'][stack['active']]

def get_result_path(current, stack):
    if "result_path" in current:
        return current['result_path']
    else:
        return get_current_frame(stack)['result_path']

f = open('prog.json', 'r')
text = json.loads(str(f.read()))
f.close()


#print(json.dumps(text))
prog = text['program']
decl = text['declarations']
stack = text['stack']
pdb.set_trace()
#next = get_next(prog['stack']['array']['active']['current_address'])
current_frame = get_current_frame(stack)
next = get_next(text, current_frame['instruction_pointer'])

#while (stack['active'] >= 0):
i=0
while (i<100):
    i+=1
    current = get_next(text, current_frame['instruction_pointer'])
    #print("1111111")
    #print(current)
    if current['type'] == "linear_add":
        left, right = binary_type(current, text)
        # не забыть если result_path нет, сделать по умолчанию 'result'
        result = left + right
        set_to_path(text, get_result_path(current, stack), result)
        # next = get_next(current['next'])
    elif current['type'] == "linear_sub":
        left, right = binary_type(current, text)
        current[current[result_path]] = left - right
        next = get_next(current['next'])
    elif current['type'] == "linear_mult":
        left, right = binary_type(current, text)
        current[current[result_path]] = left * right
        next = get_next(current['next'])
    # не забыть про дробные
    elif current['type'] == "linear_div":
        left, right = binary_type(current, text)
        current[current[result_path]] = left / right
        next = get_next(current['next'])
    elif current['type'] == "linear_and":
        left, right = binary_type(current, text)
        current[current[result_path]] = left and right
        next = get_next(current['next'])
    elif current['type'] == "linear_or":
        left, right = binary_type(current, text)
        current[current[result_path]] = left or right
        next = get_next(current['next'])
    elif current['type'] == "linear_more":
        left, right = binary_type(current, text)
        current[current[result_path]] = left > right
        next = get_next(current['next'])
    elif current['type'] == "linear_less":
        left, right = binary_type(current, text)
        current[current[result_path]] = left < right
        next = get_next(current['next'])
    elif current['type'] == "linear_equal":
        left, right = binary_type(current, text)
        current[current[result_path]] = left == right
        next = get_next(current['next'])
    elif current['type'] == "linear_if":
        if current['condition']['type'] == "pointer":
            condition = get_by_path(text, current['condition']['path'])
            if condition == True:
                next = get_next(current['if_true']['next'])
            if condition == False:
                next = get_next(current['if_false']['next'])
    elif current['type'] == "linear_input":
        print(data)
        address = input('input address (without key data, example:"number4" ): ')
        user_input = input('input data: ')
        set_to_path(data, address.split(':'), user_input)
        next = get_next(current['next'])
    elif current['type'] == "linear_goto":
        next = get_next(current['address'])
    elif current['type'] == "linear_call":
        current_frame = get_current_frame(stack)
        new_stack_element = { "instruction_pointer" : copy.deepcopy(current_frame['this']) + [current['path']] + [-1],
                              "this" : copy.deepcopy(current_frame['instruction_pointer']),
                              "result_path" : current['result_path'] }
        current_frame['instruction_pointer'][-1] += 1
        stack_push(new_stack_element)
        stack['active'] = 0
    else:
        current_frame = get_current_frame(stack)
        new_stack_element = { "instruction_pointer" : ["declarations", current['type'], -1], "this" : copy.deepcopy(current_frame['instruction_pointer'])}
        current_frame['instruction_pointer'][-1] += 1
        stack_push(new_stack_element)
        stack['active'] = 0
    current_frame = get_current_frame(stack)
    current_frame['instruction_pointer'][-1] += 1
    next = get_next(text, current_frame['instruction_pointer'])
    print(i)
    if next == "end":
        print(i)
        current_frame = get_current_frame(stack)
        del current_frame['instruction_pointer']
        while not("instruction_pointer" in current_frame):
            stack['active'] += 1
            current_frame = get_current_frame(stack)


print("\n\n\n")
print(json.dumps(text))
