from PIL import Image
import numpy as np
import cv2
import pyautogui



def get_photo(driver):
  window_size = driver.get_window_rect()
  screenshot = pyautogui.screenshot(region=(window_size['x'], window_size['y'], window_size['width'], window_size['height']))
  screenshot.save("tinderphoto.jpg")

def prepare(image_path = "tinderphoto.jpg"):
  img = Image.open(image_path).convert('RGB')
  left_upper = (610, 370)  # (x, y)
  right_lower = (975, 850)  # (x, y)


  cropped_img = img.crop((*left_upper, *right_lower))
  cropped_img.save("cropped.jpg")



def resize_and_normalize_image(image, target_size=(256, 256)):
    image_array = np.array(image)
    resized_image = cv2.resize(image_array, target_size)
    normalized_image = resized_image / 255.0
    normalized_image=np.expand_dims(normalized_image, axis=0)
    return normalized_image



