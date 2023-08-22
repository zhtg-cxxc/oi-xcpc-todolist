import re, os
from function import *
from spider.template import Spider_Base as Spider

########## LOJ - begin ##########

class Spider_LOJ(Spider):
	OJ_NAME = "LOJ"
	BASE_URL = "https://loj.ac"
	PROBLEM_URL = "/problem/{id}"
	CONFIG_NAME = "loj"
	
	def split_problem_list(self, text):
		id_list = [
			it[7:-9]
			for it in re.findall(r'<td><b>[0-9]+</b></td>', text)
		]
		name_list = [
			it.split('>')[-1][:-1]
			for it in re.findall(r'<a style="vertical-align: middle; " href="/problem/[0-9]*">[\s\S]*?\n', text)
		]
		return {
			'LOJ #' + id_list[i]: name_list[i]
			for i in range(len(id_list))
		}

	def split_max_page(self, text):
		result = 0
		base_result = re.findall(r'<a class="item" href="/problems\?page=[0-9]*">[0-9]*</a>', text)
		for it in base_result:
			page = int(it.split('<')[-2].split('>')[-1])
			if page > result:
				result = page
		return result

	def get_problem_list(self):
		e_info('downloading problem list of loj')
		req = request_get(self.BASE_URL + 'problems')
		max_page = self.split_max_page(req.text)
		result = self.split_problem_list(req.text)
		for page in range(2, max_page + 1):
			req = request_get(self.BASE_URL + 'problems?page=%d' % page)
			result.update(self.split_problem_list(req.text))
		e_info('downloaded problem list of loj, there are %d pages and %d problems' % (max_page, len(result)))
		return result

	def get_ac_list(self, user):
		url = self.BASE_URL + 'find_user?nickname={id}'.format(id=user.id)
		req = request_get(url, cookies=user.cookie)
		base_result = re.findall(r'<a href="/problem/[0-9]*">[0-9]*</a>', req.text)
		result = { 'LOJ #' + it.split('>')[1].split('<')[0] for it in base_result }
		return result

########## LOJ - end ##########