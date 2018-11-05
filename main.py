from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
import urllib.request
import time

class InstagramBot():
    def __init__(self, email, password):
        chrome_options = Options()
        #chrome_options.add_argument("--headless")
        self.browser = webdriver.Chrome(chrome_options=chrome_options)
        self.email = email
        self.password = password

    def signIn(self):
        self.browser.get('https://www.instagram.com/accounts/login/')

        emailInput = self.browser.find_elements_by_css_selector('form input')[0]
        passwordInput = self.browser.find_elements_by_css_selector('form input')[1]

        emailInput.send_keys(self.email)
        passwordInput.send_keys(self.password)
        passwordInput.send_keys(Keys.ENTER)

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
        self.browser.get('https://www.instagram.com/p/BpsdJ56gnfZ/')

        #loads all comments by clicking load more button
        loadmore_XP = "//button[contains(@class,'Z4IfV _0mzm- sqdOP yWX7d        ')]"
        loadmorebutton = self.browser.find_element_by_xpath(loadmore_XP)
        while True :
            try:
                loadmorebutton = self.browser.find_element_by_xpath(loadmore_XP)
                loadmorebutton.click()
                time.sleep(1)
            except NoSuchElementException:
                break

        #gets usernames
        username_XP = "//a[contains(@class,'FPmhX notranslate TlrDj')]"
        users = self.browser.find_elements_by_xpath(username_XP)
        for user in users:
            print(user.get_attribute('title'))


bot = InstagramBot("alikocakacgun", "SelambenHick")

bot.getComments()
