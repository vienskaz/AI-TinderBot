from PIL import Image
from preparephoto import get_photo,prepare,resize_and_normalize_image
from tensorflow import keras
import numpy as np
import time
from selenium.webdriver.common.by  import By
import os
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def bot(driver):
  get_photo(driver)
  prepare()
  normalized_photo=resize_and_normalize_image(Image.open("cropped.jpg"))
  model=keras.models.load_model("blonde_detector_vgg16.h5")
  #you can change the model to suit your needs
  y_pred=model.predict(normalized_photo)
  result = np.argmax(y_pred, axis=1)
  print(result)
  print(y_pred)

  if np.array_equal(result, np.array([1])):
    print("Blonde")
    like= driver.find_element(By.CSS_SELECTOR, "path[d='M21.994 10.225c0-3.598-2.395-6.212-5.72-6.212-1.78 0-2.737.647-4.27 2.135C10.463 4.66 9.505 4 7.732 4 4.407 4 2 6.62 2 10.231c0 1.52.537 2.95 1.533 4.076l8.024 7.357c.246.22.647.22.886 0l7.247-6.58.44-.401.162-.182.168-.174a6.152 6.152 0 0 0 1.54-4.09']")
    like.click()
    

  else:
    print('Not blonde')
    dislike=driver.find_element(By.CSS_SELECTOR, "path[d='m15.44 12 4.768 4.708c1.056.977 1.056 2.441 0 3.499-.813 1.057-2.438 1.057-3.413 0L12 15.52l-4.713 4.605c-.975 1.058-2.438 1.058-3.495 0-1.056-.813-1.056-2.44 0-3.417L8.47 12 3.874 7.271c-1.138-.976-1.138-2.44 0-3.417a1.973 1.973 0 0 1 3.25 0L12 8.421l4.713-4.567c.975-1.139 2.438-1.139 3.413 0 1.057.814 1.057 2.44 0 3.417L15.44 12Z']")
    dislike.click()
    
  os.remove("tinderphoto.jpg")
  os.remove("cropped.jpg")
  time.sleep(2)

  try:
    WebDriverWait(driver, 3).until(
        EC.presence_of_element_located((By.CLASS_NAME, "l17p5q9z"))
    )
    pop_up=driver.find_element(By.CLASS_NAME, "l17p5q9z")
    pop_up.click()
  except:
    time.sleep(1)














