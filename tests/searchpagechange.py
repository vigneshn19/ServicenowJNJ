from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from webelementpage.searchpage import SearchPage
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import logging
import time

class Searchpagechange:

    def __init__(self, driver):
        self.driver = driver

    def Searchpage_func(self, searchvalue):
        
        sp = SearchPage(self.driver)
        logging.info("An object is created for search page webelement")
        retry = 0
        while(retry < 3):
            try: 
                alert = self.driver.switch_to.alert
                logging.info("driver is switched to alert")
                alert.accept()
                logging.info("Alert is accepted")
            except NoAlertPresentException:
                pass
            try:
                searchnumber = sp.searchReqNumber_element()
                time.sleep(2)
                searchnumber.clear()
                time.sleep(3)
                searchvalue = searchvalue.upper()
                searchnumber.send_keys(searchvalue)
                logging.info("The change request searched is: %s",searchvalue)
                exactmatch = sp.exactmatch_element()
                if(exactmatch != None):
                    time.sleep(2)
                    exactmatch.click()
                    logging.info("The exact match is clicked")
                    return True
            except NoSuchElementException: 
                logging.warning("There is no such element exception")
                retry = retry+1
                logging.info("Total Number of Retries: %s", retry)
                self.driver.refresh()
                logging.info("The page is refreshed")
                time.sleep(3)
            except Exception as e:
                logging.error(f'An unexpected error occured: {e}')
        return False


        