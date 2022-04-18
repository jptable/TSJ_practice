# Action Chains
import selenium
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

s = Service("D:/Chrome_driver/chromedriver.exe")
driver = webdriver.Chrome(service = s)
url = "https://tsj.tw/"
driver.get(url)

blow = driver.find_element(By.ID, "click")
blow_count = driver.find_element(By.XPATH, "//*[@id='app']/div[2]/div[4]/div[2]/h4[2]")

items = []
items.append(driver.find_element(By.XPATH, "//*[@id='app']/div[2]/div[4]/div[4]/table/tbody/tr[4]/td[5]/button[1]"))
items.append(driver.find_element(By.XPATH, "//*[@id='app']/div[2]/div[4]/div[4]/table/tbody/tr[3]/td[5]/button[1]"))
items.append(driver.find_element(By.XPATH, "//*[@id='app']/div[2]/div[4]/div[4]/table/tbody/tr[2]/td[5]/button[1]"))

price = []
price.append(driver.find_element(By.XPATH, "//*[@id='app']/div[2]/div[4]/div[4]/table/tbody/tr[4]/td[4]"))
price.append(driver.find_element(By.XPATH, "//*[@id='app']/div[2]/div[4]/div[4]/table/tbody/tr[3]/td[4]"))
price.append(driver.find_element(By.XPATH, "//*[@id='app']/div[2]/div[4]/div[4]/table/tbody/tr[2]/td[4]"))


action = ActionChains(driver)

for i in range(1000):
    action.click(blow)
    action.perform()
    count = (blow_count.text.replace("您目前擁有", ""))
    count = int(count.replace("技術點", ""))
    for j in range(3):
        prices = int(price[j].text.replace(" 技術點", ""))
        if prices <= count:
            upgrade_action = ActionChains(driver)
            upgrade_action.move_to_element(items[j])
            upgrade_action.click()
            upgrade_action.perform()
            break