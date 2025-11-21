from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains

class Selectmac():
    def __init__(self, driver):
        self.driver = driver
        self.goto_mac = (By.CSS_SELECTOR, "#header > div > full-menu > ul > li:nth-child(3)")
        self.open_mac = (By.CSS_SELECTOR, "#product-grid > li:nth-child(1) > product-card > div")
        self.xarakter = (By.CSS_SELECTOR,"#shopify-section-template--23332115415338__245ee280-dfa9-4791-91ed-b65a153cc976 > div > div > div > tabbed-content > scroll-shadow > div > button:nth-child(2)")
        self.gohome = (By.CSS_SELECTOR, "#header > div > a")
        self.gohome2 = (By.CSS_SELECTOR, "#header > div > a")


    def safe_click(self, locator, timeout=10):
        wait = WebDriverWait(self.driver, timeout)
        element = wait.until(EC.presence_of_element_located(locator))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        ActionChains(self.driver).move_to_element(element).click().perform()

    def click_goto_mac(self):
        self.safe_click(self.goto_mac, timeout=5)

    def click_open_mac(self):
        self.safe_click(self.open_mac, timeout=10)

    def click_xarakter(self):
        self.safe_click(self.xarakter, timeout=10)

    def click_gohome(self):
        self.safe_click(self.gohome, timeout=5)
    def click_gohome2(self):
        self.safe_click(self.gohome2, timeout=5)



