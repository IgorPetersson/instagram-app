from lib2to3.pgen2 import driver
from time import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import csv

def access_instagram(driver: webdriver.Chrome, profile):
    time.sleep(5)
    driver.find_element(By.CSS_SELECTOR , "form div div:nth-child(1) label input").send_keys(profile["username"])
    driver.find_element(By.CSS_SELECTOR , "form div div:nth-child(2) label input").send_keys(profile["password"])
    driver.find_element(By.CSS_SELECTOR , "form div div:nth-child(3) button").click()
    time.sleep(5)

def recuse_questions(driver: webdriver.Chrome):
    driver.find_element(By.CSS_SELECTOR, "._ac8f button").click()
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, "._a9-z button").click()
    time.sleep(2)

def mark_people(driver: webdriver.Chrome, text: str):
    time.sleep(15)
    driver.find_element(By.CSS_SELECTOR, "form textarea").click()
    time.sleep(15)
    driver.find_element(By.CSS_SELECTOR, "form textarea").send_keys(text)
    time.sleep(15)
    driver.find_element(By.CSS_SELECTOR, "form div div:nth-child(3) div").click()
    time.sleep(20)
    driver.find_element(By.CSS_SELECTOR, "form textarea").click()
    driver.find_element(By.CSS_SELECTOR, "form textarea").send_keys("ig")
    driver.find_element(By.CSS_SELECTOR, "form textarea").send_keys(Keys.CONTROL + "a")
    driver.find_element(By.CSS_SELECTOR, "form textarea").send_keys(Keys.DELETE)
    time.sleep(80)

def separate_profiles(profiles: list[str], number_of_persons: int) -> list[str]:
    start = 1
    end = ((len(profiles)-1)//number_of_persons) * number_of_persons 
    new_profiles = []

    while end >= start:
        new_profiles.append(profiles[start:start+number_of_persons]) 
        start = start+number_of_persons   
        
     
    return new_profiles

def like_post(driver: webdriver.Chrome):
    time.sleep(4)
    driver.find_element(By.CSS_SELECTOR, "div section span button").click()
    time.sleep(2)

def follow_person(driver: webdriver.Chrome):
    time.sleep(2)
    driver.get("https://www.instagram.com/topcarcentroauto/")
    time.sleep(5)
    driver.find_element(By.CSS_SELECTOR, "header section div div div div:nth-child(2) button").click()
    time.sleep(2)
    driver.back()
    time.sleep(3)

profiles = [
    {"url": "/home/igorpetersson/repos/projects/instagram-app/profiles/profiles_igor_cardoso_santos12.txt", "id":0, "username": "igor_cardoso_santos12","password": "Aa1233212"},
    {"url": "/home/igorpetersson/repos/projects/instagram-app/profiles/profiles_igorpetersson.txt","id": 1,"username": "igorpetersson", "password": "Aa1233212"},
    {"url": "/home/igor/instagram-app/profiles/profiles_igor_santos2407.txt","id": 2,"username": "igor_santos2407", "password": "a1233212"},
    {"url": "/home/igor/instagram-app/profiles/profiles_hyago.txt", "id":3,"username": "hyago.nascimento@sou.ufmt.br", "password": "Jesusmeutudo1@"},
    {"url": "/home/igor/instagram-app/profiles/profiles_hyago.txt", "id":4,"username": "ovadushi", "password": "v81341819v"}
] 

profile = profiles.__getitem__(1)

driver = webdriver.Chrome()
driver.get("https://www.instagram.com/")

access_instagram(driver, profile)
time.sleep(6)

driver.get("https://www.instagram.com/p/CwfvO-cO-Lr/")

profiles_csv =  open(profile["url"])
profiles_reader = csv.reader(profiles_csv)
profiles = [x[0] for x in profiles_reader]

new_profiles = separate_profiles(profiles, 2)

cont = 1
for profile in new_profiles:
    text = " ".join(profile)  
    mark_people(driver, text)
    if cont > 100:
        break
    print(f"CONT {cont} - {text}")
    cont = cont + 1

time.sleep(30)

driver.close()

    