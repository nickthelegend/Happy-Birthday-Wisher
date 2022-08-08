
from selenium import webdriver
import time
browser = webdriver.Chrome('chromedriver.exe')
browser.get('https://www.instagram.com/accounts/login/')
time.sleep(4) 
#Automating the login
def login():#/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[1]/div/label/input
    Username=browser.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div[1]/div/form/div/div[1]/div/label/input")
    Username.send_keys("USERNAME")
    time.sleep(4)
    password=browser.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div[1]/div/form/div/div[2]/div/label/input")
    password.send_keys("pASS")
    password.submit()
    time.sleep(5)
#Automate the notifications
# # def notification():
#     try: 
#         
#         Notnow=browser.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div/div/button")
#         Notnow.click()  
#         time.sleep(3)
#         Noti=browser.find_element_by_xpath("/html/body/div[4]/div/div/div/div[3]/button[2]")
#         Noti.click()
#         time.sleep(7)
#     except:
#         print("BADAm")
#click the message
def message():
    msgclick=browser.find_element_by_class_name('xWeGp')
    msgclick.click()
    time.sleep(7)
    Notnow=browser.find_element_by_xpath("/html/body/div[6]/div/div/div/div[3]/button[2]")
    Notnow.click()  
    time.sleep(3)
    
def  final():
    chat=browser.find_element_by_xpath('/html/body/div[1]/section/div/div[2]/div/div/div[2]/div/div[3]/div/button')
    chat.click()
    time.sleep(7)
    typename=browser.find_element_by_xpath('/html/body/div[6]/div/div/div[2]/div[1]/div/div[2]/input')
    typename.send_keys('nxfxrin_')
    time.sleep(7)
    name=browser.find_element_by_xpath('/html/body/div[6]/div/div/div[2]/div[2]/div[1]/div')
    name.click()
    time.sleep(7)
    next=browser.find_element_by_class_name('rIacr').click()
    time.sleep(7)
    mbox = browser.find_element_by_tag_name('textarea')
    time.sleep(3)

    mbox.send_keys('HAPPY BIRTHDAY BRO Tommrow Give me 2 Chocolates!! Cya Gn')
    time.sleep(3)

    send=browser.find_element_by_xpath('/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]/button').click()
login()
# notification()
message()
final()