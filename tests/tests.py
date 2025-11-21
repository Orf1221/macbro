import pytest
import time
from selenium.common.exceptions import TimeoutException
from pages.selectmac import Selectmac
from pages.buy import Buy

def test_select_mac(driver_chrome):
    driver_chrome.get("https://macbro.uz/")
    selectmac = Selectmac(driver_chrome)
    buy = Buy(driver_chrome)

    selectmac.click_goto_mac()
    # time.sleep(1)
    # selectmac.click_open_mac()
    # time.sleep(1)
    # selectmac.click_xarakter()
    # time.sleep(5)
    selectmac.click_gohome()
    time.sleep(1)
    selectmac.click_gohome2()
    time.sleep(1)

    buy.click_gosearch()
    time.sleep(5)

    buy.input_iphone("iphone")
    time.sleep(5)
