#! python3

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

import time

import os
dir_path = os.path.dirname(os.path.realpath(__file__))

def send_msg(names, fname):

    # Replace below path with the absolute path
    # to chromedriver in your computer
    driver = webdriver.Chrome(dir_path + '/chromedriver')

    driver.get("https://web.whatsapp.com/")
    wait = WebDriverWait(driver, 600)

    # Replace 'Friend's Name' with the name of your friend
    # or the name of a group
    targets = names

    # Replace the below string with your own message
    string = "Birthdays are a new start; fresh beginnings, a time to start new endeavours with new goals. Move forward with fresh confidence and courage. You are a special person, may you have an amazing today and year. Happy birthday " + fname
    group_t = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div._1c8mz")))
    time.sleep(3)

    for target in targets:
        try:
            for person in driver.find_elements_by_class_name('X7YrQ'):      #list groups or persons in chating section

                title = person.find_element_by_xpath('div/div/div[2]/div[1]/div[1]/span').text      #get title of person or groups

                time.sleep(1)
                if '"' + title + '"' == target:
                    x_arg = '//span[contains(@title,' + target + ')]'
                    group_title = wait.until(EC.presence_of_element_located((By.XPATH, x_arg)))     #select person or group

                    group_title.click()

                    message = driver.find_elements_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')[0]

                    message.send_keys(string)

                    sendbutton = driver.find_elements_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button')[0]
                    sendbutton.click()
                    time.sleep(3)
        except:
            continue

    driver.close()
