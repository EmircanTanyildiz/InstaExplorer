import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import passw
info = passw.myInfo() #şifre alındı
def bekle(a):
    c=0
    while c<a:
        time.sleep(1)
        c += 1
        print(f'{c} sn.')
class Instagram:
    def __init__(self,username,password):
        self.browser = webdriver.Chrome()
        self.username = username
        self.password = password
    def signIn(self):
        self.browser.get("https://www.instagram.com/")
        self.browser.maximize_window()
        time.sleep(1)
        emailInput = self.browser.find_element(By.XPATH,'//*[@id="loginForm"]/div/div[1]/div/label/input')
        passwordInput = self.browser.find_element(By.XPATH,'//*[@id="loginForm"]/div/div[2]/div/label/input')
        emailInput.send_keys(self.username)
        passwordInput.send_keys(self.password)
        passwordInput.send_keys(Keys.ENTER)
        time.sleep(5)
    def getFollowing(self):
        self.browser.get(f"https://www.instagram.com/{self.username}")
        bekle(3)
        followingLink = self.browser.find_element(By.XPATH,'/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/header/section/ul/li[3]/a')
        followingLink.click()
        bekle(3)

    def getFollowers(self):
        self.browser.get(f"https://www.instagram.com/{self.username}")
        time.sleep(5)
        kacTakipciVar = self.browser.find_element(By.XPATH,'/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/header/section/ul/li[2]/a/span/span').text
        kacTakipciVar = int(kacTakipciVar)
        print(f"{kacTakipciVar} ADET TAKİPÇİN VARMIŞ (kutucuk sayısı üzerinden alındı)")
        followerlink = self.browser.find_element(By.XPATH,'/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/header/section/ul/li[2]/a')
        followerlink.click() #Takipçi kutusu açıldı
        time.sleep(3) #3 saniye bekledik her şey yüklendi
        # dialog = self.browser.find_element(By.CSS_SELECTOR,'div[role=dialog] div')
        dialog = self.browser.find_element(By.CSS_SELECTOR, 'body > div.x1n2onr6.xzkaem6 > div.x9f619.x1n2onr6.x1ja2u2z > div > div.x1uvtmcs.x4k7w5x.x1h91t0o.x1beo9mf.xaigb6o.x12ejxvf.x3igimt.xarpa2k.xedcshv.x1lytzrv.x1t2pt76.x7ja8zs.x1n2onr6.x1qrby5j.x1jfb8zj > div > div > div > div > div.x7r02ix.xf1ldfh.x131esax.xdajt7p.xxfnqb6.xb88tzc.xw2csxc.x1odjw0f.x5fp0pe > div > div > div._aano > div:nth-child(1) > div div')
        followerCount = len(dialog.find_elements(By.XPATH, '//div[@class="x1dm5mii x16mil14 xiojian x1yutycm x1lliihq x193iq5w xh8yej3"]/div'))
        print(f"kaç tanesini görüyor]: {followerCount}")
        action = webdriver.ActionChains(self.browser)
        bekle(2)
        followers = self.browser.find_element(By.CSS_SELECTOR, 'body > div.x1n2onr6.xzkaem6 > div.x9f619.x1n2onr6.x1ja2u2z > div > div.x1uvtmcs.x4k7w5x.x1h91t0o.x1beo9mf.xaigb6o.x12ejxvf.x3igimt.xarpa2k.xedcshv.x1lytzrv.x1t2pt76.x7ja8zs.x1n2onr6.x1qrby5j.x1jfb8zj > div > div > div > div > div.x7r02ix.xf1ldfh.x131esax.xdajt7p.xxfnqb6.xb88tzc.xw2csxc.x1odjw0f.x5fp0pe > div > div > div._aano > div:nth-child(1) > div').find_elements(By.XPATH, '//div[@class="x1dm5mii x16mil14 xiojian x1yutycm x1lliihq x193iq5w xh8yej3"]/div')
        linkim = self.browser.find_elements(By.TAG_NAME, 'a')
        targetClass = "x1i10hfl xjbqb8w x6umtig x1b1mbwd xaqea5y xav7gou x9f619 x1ypdohk xt0psk2 xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x16tdsg8 x1hl2dhg xggy1nq x1a2a7pz notranslate _a6hd"
        myFollowers = []
        bekle(2)
        # dialog = self.browser.find_element(By.CSS_SELECTOR,'body > div.x1n2onr6.xzkaem6 > div.x9f619.x1n2onr6.x1ja2u2z > div > div.x1uvtmcs.x4k7w5x.x1h91t0o.x1beo9mf.xaigb6o.x12ejxvf.x3igimt.xarpa2k.xedcshv.x1lytzrv.x1t2pt76.x7ja8zs.x1n2onr6.x1qrby5j.x1jfb8zj > div > div > div > div > div.x7r02ix.xf1ldfh.x131esax.xdajt7p.xxfnqb6.xb88tzc.xw2csxc.x1odjw0f.x5fp0pe > div > div > div._aano > div:nth-child(1) > div > div:nth-child(1) > div > div > div > div.x9f619.x1n2onr6.x1ja2u2z.xdt5ytf.x2lah0s.x193iq5w.xeuugli.xamitd3.x78zum5 > div > div > div > div')
        # dialog.click()
        bekle(1)
        pop_up_window = WebDriverWait(self.browser, 2).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='_aano']")))
        CC = 0
        dialog = self.browser.find_element(By.CSS_SELECTOR,'body > div.x1n2onr6.xzkaem6 > div.x9f619.x1n2onr6.x1ja2u2z > div > div.x1uvtmcs.x4k7w5x.x1h91t0o.x1beo9mf.xaigb6o.x12ejxvf.x3igimt.xarpa2k.xedcshv.x1lytzrv.x1t2pt76.x7ja8zs.x1n2onr6.x1qrby5j.x1jfb8zj > div > div > div')
        
        
        while CC < 25:
            bekle(3)
            print("döngüye girildi")
            followerCount = len(dialog.find_elements(By.XPATH, '//div[@class="x1dm5mii x16mil14 xiojian x1yutycm x1lliihq x193iq5w xh8yej3"]/div'))
            print(f"follower count: {followerCount}")
            abc = 0
            linkim = self.browser.find_elements(By.TAG_NAME, 'a')
            targetClass = "x1i10hfl xjbqb8w x6umtig x1b1mbwd xaqea5y xav7gou x9f619 x1ypdohk xt0psk2 xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x16tdsg8 x1hl2dhg xggy1nq x1a2a7pz notranslate _a6hd"
            for link in linkim:
                if abc != kacTakipciVar:
                    link_text = link.text
                    if "/www.instagram.com/" in link.get_attribute("href") and targetClass in link.get_attribute("class") and "Senin için öneriliyor" not in link_text:
                        userlar = link.get_attribute("href").replace("https://www.instagram.com/","")
                        userlar = userlar.rstrip("/")
                        print(userlar)
                        myFollowers.append(userlar)
                        abc += 1
            bekle(1)
            self.browser.execute_script('arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight;',pop_up_window)
            print("sayfa kaydırıldı")
            CC += 1
        return myFollowers
    def browserClose(self):
        self.browser.close()
emirCan = Instagram(info.username,info.password)
emirCan.signIn()
# emirCan.getFollowing()
takipciListem = emirCan.getFollowers() 
print(len(takipciListem))
takipciListem = set(takipciListem)
print(len(takipciListem))
print(takipciListem)
emirCan.browserClose()
