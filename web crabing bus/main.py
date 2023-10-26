
# This code can't scroll. so user should have to scroll while code is executing

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate('treatment-97281-firebase-adminsdk-ba112-c7823d2208.json')

firebase_admin.initialize_app(cred, {
    'databaseURL': "https://treatment-97281-default-rtdb.firebaseio.com"
})

ref = db.reference('/bus')


def my_function():
    link = "https://rongdhonustudio.com/DhakaBus.html"
    driver.get(link)
    data1 = driver.find_elements(By.XPATH, "//ul//li")
    data2 = driver.find_elements(By.XPATH, "//ul//li//div//div")

    print(f"total number of item: {len(data1)}")
    for i in range(len(data1)):
        BussName = data1[i].text
        var = data1[i]
        data1[i].click()
        time.sleep(1)
        Route = data2[i].text
        Route_name = Route.replace('Route:','')
        print(BussName, "==", Route_name)
        print(" ")


        ref.push().set({
            'bus_name': BussName,
            'bus_route': Route_name
        })


driver = webdriver.Chrome()
time.sleep(2)

my_function()

time.sleep(2)
driver.quit()
