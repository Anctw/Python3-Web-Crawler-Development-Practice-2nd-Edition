import time
import re
import tesserocr
from selenium import webdriver
from io import BytesIO
from PIL import Image
from retrying import retry
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import numpy as np

"""4.识别测试"""
# image = Image.open('./captcha.png')
# result = tesserocr.image_to_text(image)
# print(result)

# print(tesserocr.file_to_text('captcha2.png'))

"""5.处理验证码"""
# image = Image.open('./captcha2.png')

# 打印图像的宽高和颜色通道 (117, 336, 4) RGBA
# print(np.array(image).shape)
# print(image.mode)

# 将颜色通道修改为L（灰度图像）
# image = image.convert('L')
# image.show()

# 将颜色通道修改为1（二值化）
# image = image.convert('1')
# image.show()

# 将图片转化为灰度图像，然后根据阈值删除图片中的干扰点
# image = Image.open('./captcha2.png')
# image = image.convert('L')
# threshold = 50
# array = np.array(image)
# array = np.where(array > threshold, 255, 0)
# image = Image.fromarray(array.astype('uint8'))
# # image.show()
# print(tesserocr.image_to_text(image))

"""6.识别实战"""


def process(image):
    image = image.convert('L')
    array = np.array(image)
    # 识别的准确率不尽人意
    array = np.where(array > 115, 255, 0)
    image = Image.fromarray(array.astype('uint8'))
    return image


@retry(stop_max_attempt_number=10, retry_on_result=lambda x: x is False)
def login():
    browser.get('https://captcha7.scrape.center')
    browser.find_element(By.CSS_SELECTOR, '.username input[type="text"]').send_keys('admin')
    browser.find_element(By.CSS_SELECTOR, '.password input[type="password"]').send_keys('admin')
    captcha1 = browser.find_element(By.CSS_SELECTOR, '#captcha')
    image = Image.open(BytesIO(captcha1.screenshot_as_png))
    image = process(image)

    # 保存处理过后的图片
    with open('captcha3.png', 'wb') as f:
        image.save(f, 'PNG')

    captcha = tesserocr.image_to_text(image)
    print(captcha)
    captcha = re.sub('[^A-Za-z0-9]', '', captcha)
    browser.find_element(By.CSS_SELECTOR, '.captcha input[type="text"]').send_keys(captcha)

    browser.find_element(By.CSS_SELECTOR, '.login').click()
    try:
        WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, '//h2[contains(.,"登录成功")]')))
        time.sleep(10)
        browser.close()
        return True
    except TimeoutException:
        return False


if __name__ == '__main__':
    browser = webdriver.Chrome()
    login()
