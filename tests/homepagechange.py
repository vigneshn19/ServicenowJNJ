from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from webelementpage.homepage import HomePage
import logging
import time

class Homepagechange:

    def __init__(self, driver):
        self.driver = driver

    def homepage_func(self):
        try:
            logging.info("The URL is launching")
            self.driver.get("https://jnjprod.service-now.com/iris")
            logging.info("The URL is launched")
            time.sleep(3)
            assert self.driver.title == "Iris - Iris"
            logging.info("The title is validated")
            time.sleep(3)
            hp = HomePage(self.driver)
            logging.info("An object is created for home page webelement")
            logging.info("Checking whether the remind me later prompt is displayed or not")
            if(hp.remindmelater_element() != None):
                logging.info("The Remind me later button is displayed")
                hp.remindmelater_element().click()
                logging.info("The Remind me later button is clicked")
                hp.closebutton_element().click()
                logging.info("The close button is displayed")
        except NoSuchElementException:
            logging.info("There is no such element exception")
        except AssertionError: 
            logging.error("The Assert for the title is failed")
        except Exception as e:
            logging.error(f'An unexpected error occured: {e}')
        finally:
            hp.itsm_element().click()
            logging.info("The itsm link is clicked")
    