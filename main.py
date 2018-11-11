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
        #chrome_options.add_argument("--headless")
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

    #get all images from hashtag
    def getImage(self):
        self.browser.get('https://www.instagram.com/explore/tags/uniday18/')
        images = self.browser.find_elements_by_tag_name('img')
        for image in images:
            print(image.get_attribute('src'))
            filename = image.get_attribute('alt')
            url = image.get_attribute('src')
            urllib.request.urlretrieve(url, filename)

    #add users names and profile picture links to .txt file
    def getUsersPic(self):
        file = open('userspiclink.txt', 'w')
        for username in self.usernames:
            user_link = ('https://www.instagram.com/{}').format(username)
            self.browser.get(user_link)
            try:
                userimage_XP = "//img[1]"
                userimage = self.browser.find_element_by_xpath(userimage_XP)
                file.write(username + " " + userimage.get_attribute('src') + '\n')
            except:
                userimage_XP = "//img[1]"
                userimage = self.browser.find_element_by_xpath(userimage_XP)
                file.write(username + " " + userimage.get_attribute('src') + '\n')
        file.close()

    def getComments(self):
        #give post url
        self.browser.get('https://www.instagram.com/p/Bp9iz-iB3Ul/')

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
            if x != "fenerlove1907": #delete your accounts name
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

bot = InstagramBot("username", "password")
bot.getComments()
bot.chooseWinner()
