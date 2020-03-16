from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import sys
sys.path.insert(0,'/Users/alansmathew/Desktop/insta_backup/')
from password import password_

page=''

def loading(classname):
	try:
		page.find_element_by_class_name(classname)
	except :
		time.sleep(0.1)
		loading(classname)

def scroll():
    loading("isgrP")
    scroll_box = page.find_element_by_class_name("isgrP")
    last_ht, ht = 0, 1
    while last_ht != ht:
        last_ht = ht
        time.sleep(1.5)
        ht = page.execute_script("""
            arguments[0].scrollTo(0, arguments[0].scrollHeight); 
            return arguments[0].scrollHeight;
            """, scroll_box)
    links = scroll_box.find_elements_by_tag_name('a')
    names = [str(name.text) for name in links if name.text != '']
    return names
    
def login(username,password):
    global page
    page = webdriver.Chrome(executable_path = '/Users/alansmathew/Desktop/instagram_bot/chromedriver')
    page.maximize_window()
    page.get('https://www.instagram.com/accounts/login/')
    time.sleep(3)
    page.find_element_by_name('username').send_keys(username)
    page.find_element_by_name('password').send_keys(password + Keys.RETURN)
    loading('s4Iyt')

def following(user):
    page.get('https://www.instagram.com/' + user)
    loading('g47SY ')
    page.find_element_by_xpath("//a[contains(@href,'/following/')]").click()
    return scroll()

def followers(user):
    page.get('https://www.instagram.com/' + user)
    loading('g47SY ')
    page.find_element_by_xpath("//a[contains(@href,'/followers/')]").click()
    return scroll()

def likePhoto(user):
    page.get('https://www.instagram.com/' + user)
    loading('g47SY ')
    amount=int(page.find_element_by_class_name('g47SY ').text)
    if(amount==0):
        return
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
        if(i==amount):
            return
        else:
            page.find_element_by_class_name('coreSpriteRightPaginationArrow').click()
        i += 1

username='alan_s_mathew'
password=password_

ch='y'
while(ch=='y' or ch=='Y'):
    choice=int(input("1) See who is not following back \n2) Like all photos of followers and following back\n3) Like all photos of followings users\n4) Like all photos of a pirticular user\n5) Exit\n\nSelect one :"))
    if(choice==1):

        login(username,password)
        following_ppl=following(username)
        followers_ppl=followers(username)
        page.close()
        not_following =[ names for names in following_ppl if names not in followers_ppl ]
        print("Not following = ",len(not_following))
        print(not_following)

    elif(choice==2):

        login(username,password)
        following_ppl=following(username)
        followers_ppl=followers(username)
        common =[ names for names in following_ppl if names in followers_ppl ]
        for i in common:
            likePhoto(i)

    elif(choice==3):

        login(username,password)
        following_ppl=following(username)
        for i in followers_ppl:
            likePhoto(i)

    elif(choice==4):

        login(username,password)
        user=raw_input("Enter a username : ")
        likePhoto(user)

    elif(choice==5):
        break

    ch = raw_input("Do you wish to continue ? ( Y | N ) : ")

print("Thanks for using this program (: ")