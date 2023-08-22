
class Spider_Base():
	OJ_NAME = "ZJUT"
	CONFIG_NAME = "zjut"
	BASE_URL = "http://www.zjutacm.cn"
	PROBLEM_URL = "/problem/{id}"
	def __init__(self):
		pass

	def __init__(self, oj_name=None, base_url=None, config_name=None):
		if not oj_name or not base_url:
			return
		if not config_name:
			config_name = oj_name
		self.OJ_NAME = oj_name
		self.BASE_URL = base_url
		self.CONFIG_NAME = config_name
	
	def split_problem_list(text):
		pass

	def split_max_page(text):
		pass

	def get_problem_list():
		pass
	
	def get_loj_ac_list(user):
		pass