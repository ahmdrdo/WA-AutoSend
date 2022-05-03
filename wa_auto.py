from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import time

opt = webdriver.EdgeOptions()
opt.add_experimental_option('excludeSwitches', ['enable-logging'])

driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()), options=opt)
driver.get('https://web.whatsapp.com/')
driver.maximize_window()
print('Please scan the QR code to login')

# I give you 10 mins to finish the login
WebDriverWait(driver, 600).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'span[data-testid="chat"]')))

with open('recipients.txt', 'r') as rec:
    recipients = rec.read().split('\n')
    
for recipient in recipients:
    search_box = driver.find_element(By.CSS_SELECTOR, '[title="Search input textbox"]')
    search_box.click()
    time.sleep(2)
    search_box.send_keys(recipient)
    driver.find_element(By.CSS_SELECTOR, "[title='"+recipient+"']").click()
    
    msg = str(open('message.txt', 'r').read()).format(name=recipient)
    msg_box = driver.find_element(By.CSS_SELECTOR, '[title="Type a message"]')
    msg_box.click()
    msg_box.send_keys(msg)
    msg.box.send_keys(Keys.ENTER)




