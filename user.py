import yaml
from function import User, Account

def load():
	text = open('config/user.yml', 'r+', encoding='utf8')
	data = yaml.load(text, yaml.FullLoader)
	result = [
		User(**it) if type(it) == dict else it
		for it in data
	]
	return result