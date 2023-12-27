from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
import io
from selenium.webdriver.chrome.service import Service
from PIL import Image
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service=Service(executable_path='chromedriver.exe')

wd = webdriver.Chrome()

def get_images_from_google(wd, delay, max_images):
    def scroll_down(wd):
        wd.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(delay)

    #adjust url to your needs
    url = "https://www.google.com/search?sca_esv=593656281&sxsrf=AM9HkKnrgIcL9CwnjTyE0LLeSyStKNI4Ig:1703548459221&q=blonde+woman+30+year+old&tbm=isch&source=lnms&sa=X&ved=2ahUKEwjg25PG5KuDAxWpJBAIHczNDroQ0pQJegQIDBAB&biw=2320&bih=1175&dpr=1.1"
    wd.get(url)

    image_urls = set()
    skips = 0

    while len(image_urls) + skips < max_images:
        scroll_down(wd)

        thumbnails = WebDriverWait(wd, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "Q4LuWd")))

        for img in thumbnails[len(image_urls) + skips:max_images]:
            try:
                img.click()
                time.sleep(delay)
            except:
                continue

            images = WebDriverWait(wd, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "sFlh5c")))
            for image in images:
                if image.get_attribute('src') in image_urls:
                    max_images += 1
                    skips += 1
                    break

                if image.get_attribute('src') and 'http' in image.get_attribute('src'):
                    image_urls.add(image.get_attribute('src'))
                    print(f"Found {len(image_urls)}")

    return image_urls


def download_image(download_path, url, file_name):
	try:
		image_content = requests.get(url).content
		image_file = io.BytesIO(image_content)
		image = Image.open(image_file)
		file_path = download_path + file_name

		with open(file_path, "wb") as f:
			image.save(f, "JPEG")

		print("Success")
	except Exception as e:
		print('FAILED -', e)

urls = get_images_from_google(wd, 1, 200)

for i, url in enumerate(urls):
	download_image("blondes/", url, "b"+str(i) + ".jpg") #adjust path to jour needs

wd.quit()