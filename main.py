from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import urllib.request
import time
import random

class InstagramBot():
    def __init__(self, email, password):
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        self.browser = webdriver.Chrome(chrome_options=chrome_options)
        self.email = email
        self.password = password
        usernames = []
        self.usernames = usernames

    def signIn(self):
        self.browser.get('https://www.instagram.com/accounts/login/')
        time.sleep(1)
        emailInput_XP = "//input[@name='username'][@type='text']"
        passwordInput_XP = "//input[@name='password'][@type='password']"
        emailInput = self.browser.find_element_by_xpath(emailInput_XP)
        passwordInput = self.browser.find_element_by_xpath(passwordInput_XP)

        emailInput.send_keys(self.email)
        passwordInput.send_keys(self.password)
        passwordInput.send_keys(Keys.ENTER)
        time.sleep(5)

    def getImage(self):
        self.browser.get('https://www.instagram.com/explore/tags/uniday18/')
        images = self.browser.find_elements_by_tag_name('img')
        for image in images:
            print(image.get_attribute('src'))
            filename = image.get_attribute('alt')
            url = image.get_attribute('src')
            urllib.request.urlretrieve(url, filename)

    def getComments(self):
        #give post url
        self.browser.get('https://www.instagram.com/p/BpzNZZMgOTx/')

        #loads all comments by clicking load more button if exists
        while True :
            try:
                loadmore_XP = "//button[contains(@class,'Z4IfV _0mzm- sqdOP yWX7d        ')]"
                loadmorebutton = self.browser.find_element_by_xpath(loadmore_XP)
                loadmorebutton.click()
                time.sleep(1.5)
            except NoSuchElementException:
                break
        #adds usernames into a list
        users_XP = "//a[contains(@class,'FPmhX notranslate TlrDj')]"
        users = self.browser.find_elements_by_xpath(users_XP)

        for user in users:
            x = user.get_attribute('title')
            self.usernames.append(x)

        #remove duplicate usernames
        self.usernames = list(set(self.usernames))
        #add usernames to .txt file
        file = open('usernames.txt', 'w')
        for username in self.usernames:
            file.write(username + "\n")
        file.close()

    def chooseWinner(self):
        randnumber = random.randint(0, len(self.usernames)-1)
        print("from " + str(len(self.usernames)) +  " participants winner is : " + self.usernames[randnumber])

bot = InstagramBot("alikocakacgun", "SelambenHick")
bot.getComments()
bot.chooseWinner()
