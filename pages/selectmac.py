from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains

class Selectmac():
    def __init__(self, driver):
        self.driver = driver
        self.all = (By.CSS_SELECTOR,"#header > div > full-menu > ul > li.menu-item-has-children.menu-item-has-megamenu > a")
        self.filtr9 =(By.CSS_SELECTOR,"#FacetFiltersForm-bar > div.thb-filter-sort-count > div.thb-filter-sort > custom-select > button")
        self.higttolow9 = (By.CSS_SELECTOR, "#FacetFiltersForm-bar > div.thb-filter-sort-count > div.thb-filter-sort > custom-select > div > scroll-shadow > ul > li:nth-child(6)")
        self.openmac9 =(By.CSS_SELECTOR, "#product-grid > li:nth-child(1) > product-card > div > a")
        self.addcard9 = (By.CSS_SELECTOR, "#AddToCart")
        self.close9 = (By.CSS_SELECTOR, "#Cart-Drawer > div > div.side-panel-header > div > side-panel-close")
        self.goto_mac = (By.CSS_SELECTOR, "#header > div > full-menu > ul > li:nth-child(3)")
        self.filtr= (By.CSS_SELECTOR, "#FacetFiltersForm-bar > div.thb-filter-sort-count > div.thb-filter-sort > custom-select > button")
        self.higttolow = (By.CSS_SELECTOR ,"#FacetFiltersForm-bar > div.thb-filter-sort-count > div.thb-filter-sort > custom-select > div > scroll-shadow > ul > li:nth-child(6) > button")
        self.openmac = (By.CSS_SELECTOR,"#product-grid > li:nth-child(1) > product-card > div > a")
        self.colorsilver =(By.CSS_SELECTOR,"#product__option--color > label:nth-child(5)")
        # self.memmac = (By.CSS_SELECTOR, "#product__option--button > label:nth-child(5)")
        self.rammac = (By.CSS_SELECTOR, "#product__option--button > label:nth-child(5)")
        self.addcard =(By.CSS_SELECTOR,"#AddToCart")
        self.close = (By.CSS_SELECTOR,"#Cart-Drawer > div > div.side-panel-header > div > side-panel-close")
        self.iphone =(By.CSS_SELECTOR,"#header > div > full-menu > ul > li:nth-child(4) > a")
        self.filtr2= (By.CSS_SELECTOR, "#FacetFiltersForm-bar > div.thb-filter-sort-count > div.thb-filter-sort > custom-select > button")
        self.higttolow2 = (By.CSS_SELECTOR, "#FacetFiltersForm-bar > div.thb-filter-sort-count > div.thb-filter-sort > custom-select > div > scroll-shadow > ul > li:nth-child(6) > button")
        self.openiphone =(By.CSS_SELECTOR, "#product-grid > li:nth-child(10) > product-card > div > a")
        self.addcard2 = (By.CSS_SELECTOR, "#AddToCart")
        self.close2 = (By.CSS_SELECTOR, "#Cart-Drawer > div > div.side-panel-header > div > side-panel-close")
        self.akse= (By.CSS_SELECTOR, "#header > div > full-menu > ul > li:nth-child(6) > a")
        self.zaryadnik = (By.CSS_SELECTOR , "#header > div > full-menu > ul > li:nth-child(6) > ul > li.active > a")
        self.filtr6 = (By.CSS_SELECTOR,"#FacetFiltersForm-bar > div.thb-filter-sort-count > div.thb-filter-sort > custom-select > button")
        self.higttolow6 = (By.CSS_SELECTOR,"#FacetFiltersForm-bar > div.thb-filter-sort-count > div.thb-filter-sort > custom-select > div > scroll-shadow > ul > li:nth-child(6)")
        self.openzaryadnik = (By.CSS_SELECTOR,"#product-grid > li:nth-child(1) > product-card > div > a")
        self.addcard3 = (By.CSS_SELECTOR, "#AddToCart")
        self.close3 = (By.CSS_SELECTOR, "#Cart-Drawer > div > div.side-panel-header > div > side-panel-close")
        self.dyson = (By.CSS_SELECTOR, "#header > div > full-menu > ul > li:nth-child(9) > a")
        self.opendyson = (By.CSS_SELECTOR, "#product-grid > li:nth-child(2) > product-card > div > a")
        self.addcard4 = (By.CSS_SELECTOR, "#AddToCart")
        self.close4 =(By.CSS_SELECTOR, "#Cart-Drawer > div > div.side-panel-header > div > side-panel-close")
        self.golden = (By.CSS_SELECTOR, "#header > div > full-menu > ul > li:nth-child(11) > a")
        self.filtr3 =(By.CSS_SELECTOR, "#FacetFiltersForm-bar > div.thb-filter-sort-count > div.thb-filter-sort > custom-select > button")
        self.higttolow3 = (By.CSS_SELECTOR, "#FacetFiltersForm-bar > div.thb-filter-sort-count > div.thb-filter-sort > custom-select > div > scroll-shadow > ul > li:nth-child(6) > button")
        self.open = (By.CSS_SELECTOR,"#product-grid > li:nth-child(1) > product-card > div > a")
        self.addcard5 = (By.CSS_SELECTOR, "#AddToCart")
        self.delete =(By.CSS_SELECTOR,"#CartDrawerItem-1 > div.product-cart-item-info > quantity-selector > button.minus")
        self.delete2 = (By.CSS_SELECTOR,"#CartDrawerItem-2 > div.product-cart-item-info > quantity-selector > button.minus")
        self.delete3 = (By.CSS_SELECTOR,"#CartDrawerItem-3 > div.product-cart-item-info > quantity-selector > button.minus")
        self.delete4 = (By.CSS_SELECTOR,"#CartDrawerItem-4 > div.product-cart-item-info > quantity-selector > button.minus")
        self.delete5= (By.CSS_SELECTOR, "#CartDrawerItem-5 > div.product-cart-item-info > quantity-selector > button.minus")
        self.submit = (By.CSS_SELECTOR,"#Cart-Drawer > div > div.side-panel-footer > div > div.cart-drawer-buttons > form > button")
        self.address = (By.CSS_SELECTOR,"#email")
        self.deliver = (By.CSS_SELECTOR,"#delivery_strategies > div > div > div._1u2aa6m3._1u2aa6ma._1u2aa6md._1u2aa6m8.yyi4nyg.yyi4nyc._1fragemov._1fragemuu > div")
        self.country = (By.CSS_SELECTOR,"#cart-link")
        self.selectcountry = (By.CSS_SELECTOR,"#Select5 > option:nth-child(239)")
        self.iname1= (By.CSS_SELECTOR, "#TextField9")
        self.iname = (By.ID, "TextField9")
        self.isurname1 = (By.CSS_SELECTOR,"#TextField10")
        self.isurname =(By.CSS_SELECTOR,"#TextField10")
        self.iaddress1 = (By.CSS_SELECTOR,"#TextField11")
        self.iaddress = (By.CSS_SELECTOR,"#TextField11")
        self.icity1 =(By.CSS_SELECTOR,"#TextField13")
        self.icity = (By.CSS_SELECTOR,"#CartSpecialInstructions")

    def click_all(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.all)).click()

    def click_filtr9(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.filtr9)).click()

    def click_higttolow9(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.higttolow9)).click()

    def click_openmac9(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.openmac9)).click()

    def click_addcard9(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.addcard9)).click()

    def click_close9(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.close9)).click()

    def click_goto_mac(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.goto_mac)).click()

    def click_filtr(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.filtr)).click()

    def click_higttolow(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.higttolow)).click()

    def click_openmac(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.openmac)).click()

    def click_colorsilver(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.colorsilver)).click()

    # def click_memmac(self):
    #     wait = WebDriverWait(self.driver, 10)
    #     wait.until(EC.element_to_be_clickable(self.memmac)).click()

    def click_rammac(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.rammac)).click()

    def click_addcard(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.addcard)).click()

    def click_close(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.close)).click()

    def click_iphone(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.iphone)).click()

    def click_filtr2(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.filtr2)).click()

    def click_higttolow2(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.higttolow2)).click()

    def click_openiphone(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.openiphone)).click()

    def click_addcard2(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.addcard2)).click()

    def click_close2(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.close2)).click()

    def click_akse(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.akse)).click()

    def click_zaryadnik(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.zaryadnik)).click()

    def click_filtr6(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.filtr6)).click()

    def click_higttolow6(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.higttolow6)).click()

    def click_openzaryadnik(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.openzaryadnik)).click()

    def click_addcard3(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.addcard3)).click()

    def click_close3(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.close3)).click()

    def click_dyson(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.dyson)).click()

    def click_opendyson(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.opendyson)).click()

    def click_addcard4(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.addcard4)).click()

    def click_close4(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.close4)).click()

    def click_golden(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.golden)).click()

    def click_filtr3(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.filtr3)).click()

    def click_higttolow3(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.higttolow3)).click()

    def click_open(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.open)).click()

    def click_addcard5(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.addcard5)).click()

    def click_delete(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.delete)).click()

    def click_delete2(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.delete2)).click()

    def click_delete3(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.delete3)).click()

    def click_delete4(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.delete4)).click()

    def click_delete5(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.delete5)).click()

    def click_submit(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.submit)).click()

    def input_address(self, address):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located(self.address)).send_keys(address)

    def click_deliver(self):
        wait = WebDriverWait(self.driver, 20)
        wait.until(EC.element_to_be_clickable(self.deliver)).click()

    def click_country(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.country)).click()

    def click_selectcountry(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.selectcountry)).click()

    def click_iname1(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.iname)).click()

    def input_iname(self, iname):
        wait = WebDriverWait(self.driver, 20)
        wait.until(EC.visibility_of_element_located(self.iname)).clear()
        wait.until(EC.visibility_of_element_located(self.iname)).send_keys(iname)

    def click_isurname1(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.isurname)).click()

    def input_isurname(self, isurname):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located(self.isurname)).send_keys(isurname)

    def click_iaddress1(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.iaddress)).click()

    def input_iaddress(self, iaddress):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located(self.iaddress)).send_keys(iaddress)

    def click_icity1(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.icity)).click()

    def input_icity(self, icity):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located(self.icity)).send_keys(icity)





        # def input_password(self, password):
        #     wait = WebDriverWait(self.driver, 10)
        #     wait.until(EC.presence_of_element_located(self.password)).send_keys(password)










