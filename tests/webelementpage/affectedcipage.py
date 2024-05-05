from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
import time

class AffectedCIPage:

    affectedcitab = '//*[@id="tabs2_list"]/span[3]/span/span[2]'
    affectedciedit = '//*[@id="sysverb_edit_m2m"]'
    removefilter = '//*[@class="sn-filter-top condition-row__remove-cell"]/button'
    searchci = '//*[@id="_cmdb_ci"]'
    save = '//*[@id="sysverb_save"]'
    addtocollection = '//*[@id="add_to_collection_button"]'
    removefromcollection = '//*[@id="remove_from_collection_button"]'
    selectci = '//*[@id="select_0"]'
    collectedci = '//*[@id="select_1"]'

    def __init__(self, driver):
        self.driver = driver

    def removefilter_element (self):
        return self.driver.find_element(By.XPATH, self.removefilter)

    def affectedcitab_element(self):
        return self.driver.find_element(By.XPATH, self.affectedcitab)

    def affectedciedit_element(self):
        return self.driver.find_element(By.XPATH, self.affectedciedit)

    def searchCI_element(self):
        return self.driver.find_element(By.XPATH, self.searchci)

    def selectCI_element(self):
        return self.driver.find_element(By.XPATH, self.selectci)

    def collectedCI_element(self):
        return self.driver.find_element(By.XPATH, self.collectedci)

    def save_element(self):
        return self.driver.find_element(By.XPATH, self.save )

    def addtocollection_element(self):
        return self.driver.find_element(By.XPATH, self.addtocollection)

    def removefromcollection_element(self):
        return self.driver.find_element(By.XPATH, self.removefromcollection)
        