from selenium.webdriver.common.by import By
from twocaptcha import TwoCaptcha
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from selenium import webdriver as wd
import chromedriver_binary
import pandas

# Fixes the problem with immediate closing of the blowser
options = wd.ChromeOptions()
options.add_experimental_option(name='detach', value=True)

# Opens the browser
wb = wd.Chrome(options=options)
wb.implicitly_wait(10)
wb.get("https://esm.ae/login")

# Login
email_adress = wb.find_element('xpath', '//*[@id="login_username"]')
email_adress.send_keys('vantamanova@yandex.ru')

password = wb.find_element('xpath', '//*[@id="login_password"]')
password.send_keys('25051990')

submit_login_button = wb.find_element(
    'xpath', '//button[@id="kt_login_signin_submit"]')
submit_login_button.click()

# "The google recaptcha is required" Problem
