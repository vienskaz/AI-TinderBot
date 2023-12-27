from selenium.webdriver.common.by  import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time


def login(driver):
  driver.get("https://accounts.google.com/v3/signin/identifier?continue=https%3A%2F%2Fwww.google.com%2F%3Fhl%3Dpl&ec=GAZAmgQ&hl=pl&ifkv=ASKXGp3hihC-0N7PL1ATD6iqActORWfhDiR7nJH6a8-5fEM8b_QjszrlZ_MSajgyFlERnLEjmv91ag&passive=true&flowName=GlifWebSignIn&flowEntry=ServiceLogin&dsh=S906933402%3A1703427959945378&theme=glif")

  email=#yours gmail email
  password=#yours gmail password


  
  time.sleep(2)
  google_email = driver.find_element(By.CLASS_NAME, "whsOnd")
  time.sleep(1)
    
  google_email.send_keys(email + Keys.ENTER)
  time.sleep(3)

  google_password = driver.find_element(By.CLASS_NAME, "whsOnd")
  google_password.send_keys(password + Keys.ENTER)
  time.sleep(3)
  driver.get("https://tinder.com/app/recs")
  time.sleep(3)

   

  WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, "//div[text()='Zaloguj się']"))
    )
  login_button = driver.find_element(By.XPATH, "//div[text()='Zaloguj się']")
  login_button.click()
  time.sleep(2)
  iframe = driver.find_element(By.XPATH, "//iframe[contains(@title, 'Okno Zaloguj się przez Google')]")
  driver.switch_to.frame(iframe)
  google_login_container = driver.find_element(By.CLASS_NAME, "LgbsSe-bN97Pc")
  google_login_container.click()
  time.sleep(5)
  driver.switch_to.default_content()
  
  WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.CLASS_NAME, "l17p5q9z"))
    )
  allow_loc=driver.find_element(By.CLASS_NAME, "l17p5q9z")
  allow_loc.click()
  time.sleep(1)
  allow_not=driver.find_element(By.CLASS_NAME, "l17p5q9z")
  allow_not.click()
  time.sleep(3)

  



  