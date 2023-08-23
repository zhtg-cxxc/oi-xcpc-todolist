import yaml
from function import Problem

def load():
	try:
		file = open('config/problem.yml', 'r+', encoding='utf-8')
		text = file.read()
		data = yaml.load(text, yaml.FullLoader)
		result = [ Problem(**it) for it in data ]
		return result
	except:
		raise
		return []

def dump(data):
	result = []
	for it in data:
		result.append(it.to_dict())
	text = yaml.dump(result, encoding='utf-8')
	file = open('config/problem.yml', 'wb')
	file.write(text)
	
def append(val):
	data = load()
	data.append(val)
	dump(data)

def delete(index):
	data = load()
	if index >= 0 and index < len(data):
		del data[index]
	dump(data)

def move_up(id):
	data = load()
	if id <= 0:
		return
	tmp = data[id - 1]
	data[id - 1] = data[id]
	data[id] = tmp
	dump(data)

def move_down(id):
	data = load()
	if id >= len(data):
		return
	tmp = data[id + 1]
	data[id + 1] = data[id]
	data[id] = tmp
	dump(data)

if __name__ == '__main__':
	append(Problem(id='LG1000'))
	for it in load():
		print(it)