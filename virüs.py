import random
from selenium import webdriver
import os
import time

def matrix():
    counter = 0
    for i in range(500):
        random_number = random.radint(1, 999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999)
        print(random_number)
        os.system("cls")
        time.sleep(0.001)
        counter += 10
driver_path = "/path/to/chromedriver"
driver = webdriver.Chrome(executable_path=driver_path)
counter = 0
for i in range(999999999999999999999999999):
    driver.get("https://www.youtube.com/@HackerPython2")
    time.sleep(0.000.00.000.000.000.000.001)
    counter += 1
matrix()
