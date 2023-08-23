import user
import config
import problem
from function import *

config.init()
from config import config

import os
import re
import yaml
import requests

from spider.loj import Spider_LOJ
from spider.uoj import Spider_UOJ
from spider.luogu import Spider_Luogu

SPIDERS = []
AVAI_SPIDERS = {}
PROB_URL = {}

def set_ac_list(user):
	if type(user) == User:
		user.ac_list = set()
		for i in range(0, len(user.account)):
			user.account[i] = set_ac_list(user.account[i])
			user.ac_list = user.ac_list | user.account[i].ac_list
		return user
	elif type(user) == Account:
		user.ac_list = AVAI_SPIDERS[user.site].get_ac_list(user)
		return user
	
def download_problem_list():
	e_info('downloading problem list, it may take a bit time')
	result = dict()
	for si in SPIDERS:
		result.update(si.get_problem_list())
	e_info('downloaded problem list')
	return result

def get_problem_list():
	if os.path.isfile('config/problem_list.yml'):
		result = yaml.load(open('config/problem_list.yml', 'r+', encoding='utf-8').read(), yaml.FullLoader)
		return result
	else:
		e_warning('problem list cache has not found, will be downloaded')
		result = download_problem_list()
		open('config/problem_list.yml', 'wb').write(yaml.dump(result, encoding='utf-8'))
		return result

def get_url(name):
	key, val = name.split(' #')
	return PROB_URL[key].format(id=val)

def get_user_set():
	e_info('downloading user set')
	user_set = user.load()
	for i in range(0, len(user_set)):
		user_set[i] = set_ac_list(user_set[i])
	e_info('downloaded user set')
	return user_set

def spider_init():
	global SPIDERS, AVAI_SPIDERS, PROB_URL
	SPIDERS = [
		#Spider_LOJ(),
		#Spider_UOJ()
		Spider_Luogu()
	]

	AVAI_SPIDERS = {}
	PROB_URL = {}
	for si in SPIDERS:
		AVAI_SPIDERS[si.CONFIG_NAME] = si
		PROB_URL[si.OJ_NAME] = si.BASE_URL + si.PROBLEM_URL
	
spider_init()
if __name__ == '__main__':
	# print(set_ac_list(User('memset0', [Account('uoj', 'only30iq')])).ac_list)
	# print(get()[0].ac_list)

	for key, val in download_problem_list().items():
		print(key, val)