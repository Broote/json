import json

def fplus(i):
	return int(i['left']) + int(i['right'])

def fminus(i):
	return int(i['left']) - int(i['right'])
	
def fmul(i):
	return int(i['left']) * int(i['right'])

def fdiv(i):
	return int(i['left']) / int(i['right'])
	
def fmore(i):
	return int(i['left']) > int(i['right'])
	
def fless(i):
	return int(i['left']) < int(i['right'])
	
def fif(i):
	# if expr(i['first')
	return 0



text = json.loads('{"program":[{"operation":"if", "first":"5<7", "second":"2-3", "third":"4-2"}, {"operation":"==", "left":"6", "right":"7"}]}')
prog = text['program']
for i in prog:
	if i['operation'] == "+":
		print(fplus(i))
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


