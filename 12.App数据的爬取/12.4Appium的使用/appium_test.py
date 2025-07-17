from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.client_config import AppiumClientConfig
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

SERVER_URL_BASE = 'http://192.168.10.180:4723/wd/hub'

desired_capabilities = {
  "platformName": "Android",
  "deviceName": "Redmi_K30_5G",
  "appPackage": "com.goldze.mvvmhabit",
  "appActivity": ".ui.MainActivity",
  "noReset": True
}


client_config = AppiumClientConfig(
    remote_server_addr=SERVER_URL_BASE,
    direct_connection=True,
    keep_alive=False,
    ignore_certificates=True,
)
driver = webdriver.Remote(
    options=UiAutomator2Options().load_capabilities(desired_capabilities),
    client_config=client_config
)

wait = WebDriverWait(driver, 30)
wait.until(EC.presence_of_all_elements_located(
  (By.XPATH, '//android.support.v7.widget.RecyclerView/android.widget.LinearLayout')))

window_size = driver.get_window_size()
width, height = window_size.get('width'), window_size.get('height')
driver.swipe(width * 0.5, height * 0.8, width * 0.5, height * 0.2, 1000)
