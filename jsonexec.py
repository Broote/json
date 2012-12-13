import json
import pdb
#pdb.set_trace()
#implemented +, -, *, /, &&, ||, >, <, ==, if

def get_by_path(data, array):
  current_path = data
  for i in range(len(array)):
    current_path = current_path[array[i]]
  return current_path

def binary_operation(current, text):
  left = current['left']
  right = current['right']
  if left['type'] == "pointer":
    left = get_by_path(text, left['path'])
    right = get_by_path(text, right['path'])
    return left, right
    
def get_next(next):
  if next == "end":
    return "end"
  elif next['type'] == "pointer":
    # возвращается text['program'][number]
    # подумать, стоит ли каждый раз передавать program
    return text[next['path'][0]][next['path'][1]]

f = open('json_prog', 'r')
text = json.loads(str(f.read()))
f.close()


print(text)
prog = text['program']
data = text['data']
# входная точка
next = prog[1]
while (next != "end"):
  current = next
  if current['operation'] == "linear_plus":
    left, right = binary_operation(current, text)
    current['result'] = left + right
    next = get_next(current['next'])
  elif current['operation'] == "linear_minus":
    left, right = binary_operation(current, text)
    current['result'] = left - right
    next = get_next(current['next'])
  elif current['operation'] == "linear_mult":
    left, right = binary_operation(current, text)
    current['result'] = left * right
    next = get_next(current['next'])
  # не забыть про дробные
  elif current['operation'] == "linear_div":
    left, right = binary_operation(current, text)
    current['result'] = left / right
    next = get_next(current['next'])
  elif current['operation'] == "linear_and":
    left, right = binary_operation(current, text)
    current['result'] = left and right
    next = get_next(current['next'])
  elif current['operation'] == "linear_or":
    left, right = binary_operation(current, text)
    current['result'] = left or right
    next = get_next(current['next'])
  elif current['operation'] == "linear_more":
    left, right = binary_operation(current, text)
    current['result'] = left > right
    next = get_next(current['next'])
  elif current['operation'] == "linear_less":
    left, right = binary_operation(current, text)
    current['result'] = left < right
    next = get_next(current['next'])
  elif current['operation'] == "linear_equal":
    left, right = binary_operation(current, text)
    current['result'] = left == right
    next = get_next(current['next'])    
  elif current['operation'] == "linear_if":
    if current['condition']['type'] == "pointer":
      condition = get_by_path(text, current['condition']['path'])
      if condition == True:
        next = get_next(current['if_true']['next'])
      if condition == False:
        next = get_next(current['if_false']['next'])  

print("finish")
print(text)
