from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import urllib.request

class InstagramBot():
    def __init__(self, email, password):
        self.browser = webdriver.Chrome()
        self.email = email
        self.password = password

    def signIn(self):
        self.browser.get('https://www.instagram.com/accounts/login/')

        emailInput = self.browser.find_elements_by_css_selector('form input')[0]
        passwordInput = self.browser.find_elements_by_css_selector('form input')[1]

        emailInput.send_keys(self.email)
        passwordInput.send_keys(self.password)
        passwordInput.send_keys(Keys.ENTER)
        time.sleep(2)

    def getImage(self):
        self.browser.get('https://www.instagram.com/explore/tags/uniday18/')
        time.sleep(2)
        images = self.browser.find_elements_by_tag_name('img')
        for image in images:
            print(image.get_attribute('src'))
            filename = image.get_attribute('alt')
            url = image.get_attribute('src')
            urllib.request.urlretrieve(url, filename)


bot = InstagramBot("alikocakacgun", "SelambenHick")
bot.signIn()
bot.getImage()
