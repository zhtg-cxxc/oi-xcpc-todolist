import re
import json, time
from function import *
from spider.template import Spider_Base as Spider
from urllib.parse import unquote

########## Luogu - begin ##########

class Spider_Luogu(Spider):
	OJ_NAME = "洛谷"
	BASE_URL = "https://www.luogu.com.cn"
	PROBLEM_URL = "/problem/{id}"
	CONFIG_NAME = "luogu"
	
	def split_problem_list(self, text):
		jsons = self.luogu_deqoute(text)["currentData"]["problems"]
		return {
			self.OJ_NAME + ' #' + it["pid"] : self.url_escape(it["title"]) for it in jsons["result"]
		}

	def get_problem_list(self):
		e_info('downloading problem list of ' + self.OJ_NAME)
		req = request_get(self.BASE_URL + '/problem/list')
		req.encoding = 'utf-8'
		decode_json = self.luogu_deqoute(req.text)["currentData"]["problems"]
		max_page = (decode_json["count"] + decode_json["perPage"] - 1) // decode_json["perPage"]
		#max_page = 1
		result = self.split_problem_list(req.text)
		for page in range(2, max_page + 1):
			time.sleep(0.1)
			req = request_get(self.BASE_URL + '/problem/list?page=%d' % page)
			req.encoding = 'utf-8'
			result.update(self.split_problem_list(req.text))
		e_info('downloaded problem list of %s, there are %d pages and %d problems' % (self.OJ_NAME, max_page, len(result)))
		return result

	def get_ac_list(self, user):
		# /html/body/div/div[2]/main/div/div[2]/section[2]/div[3]
		url = self.BASE_URL + '/user/{id}#practice'.format(id=user.id)
		req = request_get(url, cookies=user.cookie)
		decode_json = self.luogu_deqoute(req.text)
		result = { self.OJ_NAME + ' #' + it["pid"] for it in decode_json["currentData"]["passedProblems"]}
		return result
	
	def luogu_deqoute(self, text):
		pattern = r'JSON\.parse\(decodeURIComponent\("(.*?)"\)\)'
		matches = re.findall(pattern, text)
		decoded_match = unquote(matches[0]).replace("\/", "/").replace("\n", "\\n")
		return json.loads(decoded_match)
	
	def url_escape(self, text):
		return text#.encode().decode('unicode_escape')

########## Luogu - end ##########

# if __name__ == "__main__":
# 	lg = Spider_Luogu()
# 	user = Account("luogu", "66715", "zhtg")
# 	# user.ac_list = lg.get_ac_list(user)
# 	# print(user.ac_list)
# 	req = request_get(lg.BASE_URL + '/problem/list?page=81')
# 	req.encoding = 'utf-8'