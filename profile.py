from lib2to3.pgen2 import driver
from time import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import csv

def access_instagram(driver: webdriver.Chrome):
    time.sleep(5)
    driver.find_element(By.CSS_SELECTOR , "form div div:nth-child(1) label input").send_keys("igor_cardoso_santos12")
    driver.find_element(By.CSS_SELECTOR , "form div div:nth-child(2) label input").send_keys("Aa1233212")
    driver.find_element(By.CSS_SELECTOR , "form div div:nth-child(3) button").click()
    time.sleep(5)

def recuse_questions(driver: webdriver.Chrome):
    driver.find_element(By.CSS_SELECTOR, "._ac8f button").click()
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, "._a9-z button").click()
    time.sleep(2)

driver = webdriver.Chrome()
driver.get("https://www.instagram.com/")

access_instagram(driver)
time.sleep(2)

driver.get("https://www.instagram.com/igor_cardoso_santos12")
time.sleep(5)

driver.find_element(By.CSS_SELECTOR, "header section ul li:nth-child(3)").click()

profiles = open("/home/igorpetersson/repos/projects/instagram-app/profiles_igor_cardoso_santos12.txt", "a", newline='', encoding='utf-8')
file = csv.writer(profiles, delimiter=" ")

time.sleep(5)

for i in range(1,1000):
    text = driver.find_element(By.CSS_SELECTOR, f"div div:nth-child(2) div div div:nth-child({i}) div:nth-child(2) div div div span").text
    profile = f"@{text}"
    file.writerow([profile])
    print(profile)
    time.sleep(1)

file.close()

driver.close()

