from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

class Buy:
    def __init__(self, driver):
        self.driver = driver
        self.gosearch= (By.CSS_SELECTOR, "#header > div > div.thb-secondary-area.thb-header-right > a.thb-secondary-area-item.thb-quick-search")
        self.put = (By.CSS_SELECTOR, "#Search-Drawer > div > div.side-panel-header > div > form > fieldset")
        self.panel = (By.CSS_SELECTOR, "#side-panel-search")

    def click_gosearch(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.gosearch)).click()

        wait.until(EC.visibility_of_element_located(self.panel))

    def input_put(self, put):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located(self.put)).send_keys(put)






