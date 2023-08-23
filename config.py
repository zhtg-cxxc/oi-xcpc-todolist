import yaml

def init():
	global config
	text = open('config/config.yml', 'r+', encoding='utf-8')
	config = yaml.load(text, yaml.FullLoader)