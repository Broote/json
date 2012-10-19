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



text = json.loads('{"program":[{"operation":"-", "left":"5", "right":"7"}, {"operation":"==", "left":"6", "right":"7"}]}')
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


