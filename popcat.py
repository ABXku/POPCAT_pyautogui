from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import pyautogui
import time

# Popcat website
website = "https://popcat.click"
#You need to change this to your own path
path = "/Users/cindyz/Applications/chromedriver-mac-x64/chromedriver"

# Add options to avoid bot detection
options = Options()
options.add_experimental_option("excludeSwitches", ['enable-automation'])
options.add_experimental_option("useAutomationExtension", False)

# Default Service instance
service = Service(executable_path=path)
driver = webdriver.Chrome(service=service, options=options)

# Navigate to Popcat website
driver.maximize_window()
driver.get(website)

screen_size = pyautogui.size()
width = screen_size[0]
height = screen_size[1]
click_position = [width/2, height/2]
try:
    while True:
        pyautogui.click(x=click_position[0], y=click_position[1])
except:
    time.sleep(3)
    screenshot = pyautogui.screenshot()
    screenshot.save("screenshot.png")