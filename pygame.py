from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Configure Selenium WebDriver
chrome_options = Options()
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--disable-extensions")

# Path to the ChromeDriver executable
webdriver_service = Service('chromedriver.exe')  # Update with the actual path to your chromedriver

driver = webdriver.Chrome(service=webdriver_service, options=chrome_options)
driver.get("https://www.crazygames.com/game/chicken-clicker")
try:
    
    # Wait for the iframe to be available and switch to it
    iframe = WebDriverWait(driver, 3).until(
        EC.presence_of_element_located((By.XPATH, "//iframe[@id='game-iframe']"))
    )
    driver.switch_to.frame(iframe)
    
    # Now interact with the button inside the iframe
    button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[2]/div/span/div[2]/button"))
    )
    if(button):
        button.click()
        print("after clicked")
        gamecontainer=WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="game-container"]/iframe')))
        #print(gamecontainer)
        driver.switch_to.frame(gamecontainer)
    gamecanvas=driver.find_element(By.TAG_NAME,'canvas')
    print(gamecanvas.tag_name)
    time.sleep(10)
    canvas_width = gamecanvas.size['width']
    canvas_height = gamecanvas.size['height']

# Calculate the center of the canvas
    center_x = canvas_width / 2
    center_y = canvas_height / 2

# Create an ActionChains object
   

# Perform a click at the center of the canvas
    num_clicks = 10000  # Number of continuous clicks
    interval = 0.001  # Time interval between clicks in seconds
    
# Perform continuous clicks
    while True:
        gamecanvas.click()
        time.sleep(interval)  # Wait for the defined interval before the next click

    input("Press Enter to close the browser...")

    # Switch back to the main content
    driver.switch_to.default_content()

except Exception as e:
    print(f"Error: {e}")
