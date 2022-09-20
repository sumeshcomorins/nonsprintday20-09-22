from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep
from openpyxl import Workbook

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get('https://www.amazon.in/')

driver.find_element(By.ID ,'twotabsearchtextbox').send_keys('samsung mobiles')

# driver.find_element(By.ID ,'nav-search-submit-button').click()

driver.find_element(By.XPATH ,"//input[@id='nav-search-submit-button']").click()
prd_name=driver.find_elements(By.XPATH ,"//span[@class='a-size-medium a-color-base a-text-normal']")
prd_price=driver.find_elements(By.XPATH ,"//span[@class='a-price-whole']")

product_name_list = []
product_price_list = []

for prod in prd_name:
        product_name_list.append(prod.text)
for price in prd_price:
        product_price_list.append(price.text)

final_list = zip(product_name_list,product_price_list)

# print(product_name_list)
# print(product_price_list)

# print(list(final_list))

wb =Workbook()
wb['Sheet'].title = 'Mobile Records'
sheet1 = wb.active

for data in list(final_list):
    sheet1.append(data)

wb.save('sample.xlsx')

file = open('sample.xlsx', 'rb')
file_data = file.read()
file_name = file.name

print(file_data)
print(file_name)


sleep(5)

# driver.quit()