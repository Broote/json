import json
import pdb #pdb.set_trace()
import copy
from functions_helper import *

SIMPLE_OPERATIONS = ["linear_add", "linear_sub", "linear_mult", "linear_div",
                    "linear_and", "linear_or", "linear_more", "linear_less", "linear_equal"]

# returns result of simple operation
def binary_operation(operation):
    left, right = binary_type(current, text)
    result = {
        'linear_add'   : left + right,
        'linear_sub'   : left - right,
        'linear_mult'  : left * right,
        'linear_div'   : left / right,
        'linear_and'   : left and right,
        'linear_or'    : left or right,
        'linear_more'  : left > right,
        'linear_less'  : left < right,
        'linear_equal' : left == right
    }[operation]
    set_to_path(text, get_result_path(current, stack), result)

f = open('prog.json', 'r')
text = json.loads(str(f.read()))
f.close()


stack = text['stack']
#pdb.set_trace()
current_frame = get_current_frame(stack)
next = get_next(text, current_frame['instruction_pointer'])

# execute while we have not empty active stack frame
while current_frame:
    current = next
    # check if we have linear_* operation from core
    if current['type'] in SIMPLE_OPERATIONS:
        binary_operation(current['type'])
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
        stack_push(text, new_stack_element)
        stack['active'] = 0
    # else it should be defined in declarations structure
    else:
        current_frame = get_current_frame(stack)
        new_stack_element = { "instruction_pointer" : ["declarations", current['type'], -1],
                            "this" : copy.deepcopy(current_frame['instruction_pointer']),
                            "result_path" : get_result_path(current, stack) }
        current_frame['instruction_pointer'][-1] += 1
        stack_push(text, new_stack_element)
        stack['active'] = 0
    current_frame = get_current_frame(stack)
    current_frame['instruction_pointer'][-1] += 1
    next = get_next(text, current_frame['instruction_pointer'])
    # if instructions in current structure finished change active frame
    while next == "end" and current_frame:
        current_frame = get_current_frame(stack)
        del current_frame['instruction_pointer']
        while (current_frame and(not("instruction_pointer" in current_frame))):
            stack['active'] += 1
            current_frame = get_current_frame(stack)
        if current_frame:
            next = get_next(text, current_frame['instruction_pointer'])


print(json.dumps(text))
print("\nresult:\n")
print(json.dumps(text['data']['RESULT']))
