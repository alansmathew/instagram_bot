from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time, sys
sys.path.insert(0,'/Users/alansmathew/Desktop/insta_backup/')
from password import password_

page=webdriver.Chrome(executable_path = '/Users/alansmathew/Desktop/instagram_bot/chromedriver')

def loading(classname):
	try: page.find_element_by_class_name(classname)
	except :
		time.sleep(0.1)
		loading(classname)

def login(username,password):
	page.get('https://www.instagram.com/accounts/login/')
	time.sleep(3)
	page.find_element_by_name('username').send_keys(username)
	page.find_element_by_name('password').send_keys(password + Keys.RETURN)
	loading("s4Iyt")

def username(user):
	page.get('https://www.instagram.com/' + user)
	loading('g47SY ')
	return int(page.find_element_by_class_name('g47SY ').text)

def likePhotos(amount):
	loading('v1Nh3')
	page.find_element_by_class_name('v1Nh3').click()
	i = 1
	while i <= amount:
		loading('_15y0l')
		def lk():
			try:
				page.find_element_by_xpath("//*[contains(@aria-label,'Like')]").click()
			except :
				return
		lk()
		page.find_element_by_class_name('coreSpriteRightPaginationArrow').click()
		i += 1
	
login('alan_s_mathew',password_)
photos=username('samkolder')
likePhotos(photos)
