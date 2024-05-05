from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
import time

class SearchPage:
    
    def __init__(self, driver):
        self.driver = driver

    def shadowroot_element(self):
        shadow_root1 = self.driver.find_element(By.CSS_SELECTOR,'body > macroponent-f51912f4c700201072b211d4d8c26010[app-id="a84adaf4c700201072b211d4d8c260b7"]').shadow_root
        shadow_root2 = shadow_root1.find_element(By.CSS_SELECTOR,'div > sn-canvas-appshell-root > sn-canvas-appshell-layout > sn-polaris-layout').shadow_root
        shadow_root3 = shadow_root2.find_element(By.CSS_SELECTOR,'div.sn-polaris-layout.polaris-enabled > div.layout-main > div.header-bar > sn-polaris-header').shadow_root
        shadow_root4 = shadow_root3.find_element(By.CSS_SELECTOR,'nav.polaris-layout > div > div.ending-header-zone > div.polaris-header-controls > div.polaris-search.polaris-enabled > sn-search-input-wrapper').shadow_root
        shadow_root5 = shadow_root4.find_element(By.CSS_SELECTOR,'sn-search-combobox').shadow_root
        shadow_root6 = shadow_root5.find_element(By.CSS_SELECTOR,'sn-search-combobox-desktop').shadow_root
        return shadow_root6

    def searchReqNumber_element(self):
        time.sleep(3)      
        searchElement = self.shadowroot_element().find_element(By.CSS_SELECTOR,'div > div > div > input')
        return searchElement

    def exactmatch_element(self):
        time.sleep(3)
        exactmatchElement = self.shadowroot_element().find_element(By.CSS_SELECTOR,'div > div > div.search-popover.-global > ul[aria-labelledby="result-section-header-0"] > span[aria-live="polite"]+li > div')
        return exactmatchElement
