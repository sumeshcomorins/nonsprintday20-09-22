from time import sleep
from selenium.webdriver.support.select import Select
from distutils.spawn import find_executable
from selenium_helpers import find_if_exists_by_xpath, initialize


try:
    global driver
    driver = initialize()
    driver.get("https://www.flipkart.com/")
    find_if_exists_by_xpath("//div/button[contains(@class, '_2KpZ6l _2doB4z')]").click()
    find_if_exists_by_xpath("//div[contains(@class, '_3OO5Xc')]/input[contains(@class, '_3704LK')]").send_keys("Mobiles")
    find_if_exists_by_xpath("//button[contains(@class, 'L0Z3Pu')]").click()
    find_if_exists_by_xpath("//div[contains(@class, '_3uDYxP')]/select[contains(@class, '_2YxCDZ')]").click()
    find_if_exists_by_xpath("//div[contains(@class, '_3uDYxP')]/select[contains(@class, '_2YxCDZ')]/option[3]").click()
    sleep(20)
    driver.close()

except Exception as e:
    print('Exception')
    print(e)