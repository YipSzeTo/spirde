from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.options import Options  # 实现无可视化界面
from selenium.webdriver import ChromeOptions  # 实现规避检测

# 无可视化界面
chrome_options = Options()
chrome_options.add_argument('--headless')  # 无头模式
chrome_options.add_argument('--disable-gpu')  # 不使用gpu加速

# 实现规避检测
chrome_options.add_experimental_option('excludeSwitches', ['enable-automation'])

# 创建一个浏览器对象
browse = webdriver.Chrome(
	executable_path='./chromedriver.exe', options=chrome_options,
)

# 加载qq网页
url = 'https://qzone.qq.com/'
browse.get(url=url)

# 标签定位
# 定位到’帐号密码登录‘
browse.switch_to.frame('login_frame')  # 定位的标签位于iframe标签之中，需使用switch_to.frame(iframe的id)
a_tag = browse.find_element_by_id('switcher_plogin')  # 使用id找标签
a_tag.click()  # 点击

# 标签定位
user_input = browse.find_element_by_id('u')
password = browse.find_element_by_id('p')
btn = browse.find_element_by_id('login_button')

# 标签交互
user_input.send_keys('1234134')  # qq账号
password.send_keys('1212')  # 密码
btn.click()  # 点击

# browse.back()  # 返回
# browse.quit()  # 退出

# 执行js脚本
# browse.execute_script('window.scrollTo(0,document.body.scrollHeight)')