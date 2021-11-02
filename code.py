from selenium import webdriver
from selenium.webdriver.common.by import By
import pickle
import time
import random
import datetime

now = datetime.datetime.now()
Dock = open("test.txt")
LastDay = Dock.read()
if int(LastDay) != now.day:  
    Today = now.day
    f = open("test.txt", "w")
    f.write(str(Today))
    f.close()
    def get_webdriver():
        option = webdriver.FirefoxOptions()
        option.set_preference('dom.webdriver.enabled',False)
        driver = webdriver.Firefox(options=option)
        return driver

    driver = get_webdriver()
    driver.get('https://monitoringminecraft.ru/top/mcskill/') 
    inputP = driver.find_elements_by_css_selector('html body div#wrapper div#content div#page div#cap form.right input')
    inputP[0].send_keys('fekki')
    inputP[1].click()
    inputVK = driver.find_elements_by_css_selector('html body div.oauth_wrap div.oauth_wrap_inner div.oauth_wrap_content div.oauth_content form#login_submit div.oauth_form div.oauth_form_login input.oauth_form_input')
    inputVK[0].send_keys('')
    inputVK[1].send_keys('')
    inputAVK = driver.find_elements_by_css_selector('html body div.oauth_wrap div.oauth_wrap_inner div.oauth_wrap_content div.oauth_content form#login_submit div.oauth_form div.oauth_form_login button#install_allow.flat_button.oauth_button.button_wide')
    inputAVK[0].click()

    driver.get('https://minecraftrating.ru/projects/mcskill/') 
    inputP1 = driver.find_elements_by_css_selector('html body div.wrapper-main div.container.page-server.project-page div.content-server div.promotion-back div.form-group.form-vote form input.form-control.input-sm')
    inputP1[0].send_keys('fekki')
    inputF1 = driver.find_elements_by_css_selector('html body div.wrapper-main div.container.page-server.project-page div.content-server div.promotion-back div.form-group.form-vote form button.btn.btn-success.btn-xs')
    inputF1[0].click()

    driver.get('https://topcraft.ru/servers/218/')
    time.sleep(10)
    inputS = driver.find_elements_by_css_selector('html body div.container.main-container.affix-top section header.project-header div.project-card div.row div.col-xs-2.project-btn.project-btn__vote-btn button.btn.btn-info.btn-vote.openLoginModal')
    inputS[0].click()
    inputVK = driver.find_elements_by_css_selector('html body.modal-open div.modal.fade.in div.modal-dialog div.modal-content div.modal-body div.usr-social-login ul.list-inline.login__social-l li a.login__social-lnk.login__social-vk.modalVkLogin')
    inputVK[0].click()

    time.sleep(2)
    inputP2 = driver.find_elements_by_css_selector("#nick")

    inputP2[0].click    
    inputP2[0].send_keys('fekki')
    time.sleep(1)
    inputkap = driver.find_elements_by_css_selector('.voteForm__captcha')

    action = webdriver.common.action_chains.ActionChains(driver)
    action.move_to_element_with_offset(inputkap[0], random.uniform(20, 30), random.uniform(30, 40) )
    print("got to the captcha")
    action.click()
    action.perform()
    time.sleep(2)
    inputF2 = driver.find_elements_by_css_selector('button.btn:nth-child(3)')

    inputF2[0].click()
    print("congratulations")
else:
    print("no relevant today")
   
    


