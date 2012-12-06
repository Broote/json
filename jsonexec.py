import json
import pdb
#pdb.set_trace()

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

f = open('json_prog', 'r')
text = json.loads(str(f.read()))
f.close()


print(text)
prog = text['program']
data = text['data']
next = prog[0]
while (next != "end"):
	current = next
	if current['operation'] == "linear_plus":
		left, right = binary_operation(current, text)
		current['result'] = left + right
		next = current['next']
	

if False: # комментарий
	if True:	
		print("abc")
	elif current['operation'] == "-":
		print(fminus(i))
	elif current['operation'] == "*":
		print(fmul(i))
	elif current['operation'] == "/":
		print(fdiv(i))
	elif current['operation'] == ">":
		print(fmore(i))
	elif current['operation'] == "<":
		print(fless(i))
	elif current['operation'] == "==":
		print(fmore(i) or fless(i) == False)
	elif current['operation'] == "if":
		print(fif(i))
