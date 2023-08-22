import yaml

def init():
	global config
	text = open('config/config.yml', 'r+', encoding='utf8')
	config = yaml.load(text, yaml.FullLoader)