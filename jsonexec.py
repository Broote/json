import json
import pdb

def get_by_path(data, array):
	current_path = data
	for i in range(len(array)):
		current_path = current_path[array[i]]
	return current_path


text = json.loads(str(open('json_prog', 'r').read()))
print(text)
prog = text['program']
data = text['data']
next = prog[0]
#while (current['operation'] != "end"):
pdb.set_trace()
while (next != "end"):
	current = next
	if current['operation'] == "linear_plus":
		left = current['left']
		right = current['right']
		if left['type'] == "pointer":
			left = get_by_path(text, left['path'])
			right = get_by_path(text, right['path'])
			current['result'] = left + right
		next = current['next']	
	

if False: # комментарий
	elif i['operation'] == "-":
		print(fminus(i))
	elif i['operation'] == "*":
		print(fmul(i))
	elif i['operation'] == "/":
		print(fdiv(i))
	elif i['operation'] == ">":
		print(fmore(i))
	elif i['operation'] == "<":
		print(fless(i))
	elif i['operation'] == "==":
		print(fmore(i) or fless(i) == False)
	elif i['operation'] == "if":
		print(fif(i))


