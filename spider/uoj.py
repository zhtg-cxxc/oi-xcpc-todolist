import re
from function import *
from spider.template import Spider_Base as Spider

########## UOJ - begin ##########

class Spider_UOJ(Spider):
	OJ_NAME = "UOJ"
	BASE_URL = "https://uoj.ac"
	PROBLEM_URL = "/problem/{id}"
	CONFIG_NAME = "uoj"
	
	def split_problem_list(self, text):
		return {
			self.OJ_NAME + ' #' + it.split('>#')[1].split('<')[0]:
			it.split('<')[-3].split('>')[-1]
			for it in re.findall(r'<td>#[0-9]*</td><td class="text-left"><a href="/problem/[0-9]*">[\s\S]*?</a></td>', text)
		}

	def split_max_page(self, text):
		base_result = re.findall(r'/problems\?page=', text)
		result = len(base_result) // 2
		return result

	def get_problem_list(self):
		e_info(f'downloading problem list of {self.CONFIG_NAME}')
		req = request_get(self.BASE_URL + '/problems')
		req.encoding = 'utf-8'
		max_page = self.split_max_page(req.text)
		result = self.split_problem_list(req.text)
		for page in range(2, max_page + 1):
			req = request_get(self.BASE_URL + '/problems?page=%d' % page)
			req.encoding = 'utf-8'
			result.update(self.split_problem_list(req.text))
		e_info(f'downloaded problem list of {self.CONFIG_NAME}, there are %d pages and %d problems' % (max_page, len(result)))
		return result

	def get_ac_list(self, user):
		url = self.BASE_URL + '/user/profile/{id}'.format(id=user.id)
		req = request_get(url, cookies=user.cookie)
		base_result = re.findall(r'<a href="/problem/[0-9]*" style="display:inline-block; width:4em;">[0-9]*</a>', req.text)
		result = { f'{self.OJ_NAME} #' + it.split('>')[1].split('<')[0] for it in base_result }
		return result

########## UOJ - end ##########