from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

class Buy:
    def __init__(self, driver):
        self.driver = driver
        self.gosearch = (By.CSS_SELECTOR, "a.thb-quick-search")
        self.put = (By.CSS_SELECTOR, "#side-panel-search-input")
        self.panel = (By.CSS_SELECTOR, "#side-panel-search")  # сама боковая панель

    def click_gosearch(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.gosearch)).click()
        # дождаться, пока панель откроется
        wait.until(EC.visibility_of_element_located(self.panel))

    def input_iphone(self, text):
        wait = WebDriverWait(self.driver, 10)
        input_box = wait.until(EC.element_to_be_clickable(self.put))
        # прокрутка и клик
        self.driver.execute_script("arguments[0].scrollIntoView(true);", input_box)
        ActionChains(self.driver).move_to_element(input_box).click().perform()
        input_box.clear()
        input_box.send_keys(text)