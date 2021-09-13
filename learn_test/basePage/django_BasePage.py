class BasePage(object):
    # 初始化
    def __init__(self, driver):
        self.base_url = 'http://127.0.0.1:8000/admin'
        self.driver = driver
        self.timeout = 1
    # 定义打开登录页面的方法
    def _open(self):
        url = self.base_url
        self.driver.get(url)
    # 定义open方法，调用_open()进行打开
    def open(self):
        self._open()

    def find_element(self, *loc):
        return self.driver.find_element(*loc)