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

ref = db.reference('/drug')


def my_function(link, count):
    driver.get(link)
    data1 = driver.find_elements(By.XPATH, "//a[@class='hoverable-block']//div[1]/div[1]")
    data2 = driver.find_elements(By.XPATH, "//a[@class='hoverable-block']//div[1]/div[1]/span")
    data3 = driver.find_elements(By.XPATH, "//a[@class='hoverable-block']//div[1]/div[2]/span")
    data4 = driver.find_elements(By.XPATH, "//a[@class='hoverable-block']//div[1]/div[3]")
    data5 = driver.find_elements(By.XPATH, "//a[@class='hoverable-block']//div[1]/div[4]/div/span")

    print(f"total number of item: {len(data1)}")
    for i in range(len(data1)):
        FullText = data1[i].text
        drug_type = data2[i].text

        drug_name = FullText.replace(drug_type, '')
        quantity = data3[i].text
        group_name = data4[i].text

        Text = data5[i].text
        pos = Text.find(":")
        y = len(Text) - 1
        print(count, ". ", drug_name, "=", group_name)

        price = Text[pos + 1:y]
        unit_type = Text[0:pos]

        ref.push().set({
            'drug_name': drug_name,
            'drug_type': drug_type,
            'quantity': quantity,
            'group_name': group_name,
            'price': price,
            'unit_type': unit_type,
            'company': "Eskayef Pharmaceuticals Ltd"
        })

        count += 1

    return count


driver = webdriver.Chrome()
time.sleep(2)
count = 1
for x in range(1, 24):
    url = "https://medex.com.bd/companies/2/aci-limited/brands?page=" + str(x)
    count = my_function(url, count)
print("total row = ", count)
time.sleep(2)
driver.quit()
