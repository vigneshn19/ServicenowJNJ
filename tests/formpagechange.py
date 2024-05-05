from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.alert import Alert
from webelementpage.formpage import FormPage
from datetime import datetime, timedelta
import logging
import time

class Formpagechange:

    def __init__(self, driver):
        self.driver = driver

    def formpage_func(self, urgencyValue,shortdescValue, descValue, assignciValue, assigngrpValue, justifyValue):
        logging.info("The web element object of form page is created")
        fp = FormPage(self.driver)

        try:
            if(fp.leavebutton_element()!=None):
                logging.info("Inside leave button shadow root")
                fp.leavebutton_element().click()
                logging.info("Leave button is clicked")
        except:
            pass

        try: 
            alert = self.driver.switch_to.alert
            logging.info("driver is switched to alert")
            alert.accept()
            logging.info("Alert is accepted")
        except NoAlertPresentException:
            pass

        try:
            iframe_spcl = fp.iframe_element()
            self.driver.switch_to.frame(iframe_spcl)
            if(fp.dismiss_element()!=None):
                logging.info("Special Handling Notes dialog box is prompted")
                fp.dismiss_element().click()
                logging.info("Special Handling Notes dialog box is closed")
        except:
            self.driver.switch_to.default_content()

        try:

            iframe = fp.iframe_element()
            self.driver.switch_to.frame(iframe)
            logging.info("The driver is switched to iframe")
            time.sleep(2)
            '''
            fp.copychangebutton_element().click()
            logging.info("The copy change button is clicked")
            time.sleep(4)
            
            urgency = fp.urgency_element()
            urgencyElement = Select(urgency)
            urgencyElement.select_by_visible_text(urgencyValue)
            logging.info("The urgency is selected from the dropdown")
            
            fp.shortdescription_element().clear()
            if(shortdescValue!=None):
                fp.shortdescription_element().send_keys(shortdescValue)
                logging.info("The Short description is added")
            
            fp.description_element().clear()
            if(descValue!=None):
                fp.description_element().send_keys(descValue)
                logging.info("The description is added")
            
            fp.assignmentci_element().clear()
            if(assignciValue!=None):
                assignciValue = assignciValue.strip()
                fp.assignmentci_element().send_keys(assignciValue)
                logging.info("The Assignment CI is added")
            
            fp.assignmentgroup_element().clear()
            if(assigngrpValue!=None):
                assigngrpValue = assigngrpValue.strip()
                fp.assignmentgroup_element().send_keys(assigngrpValue)
                logging.info("The Assignment group is added")
            
            time.sleep(2)
            fp.planningtab_element().click()
            logging.info("The Planning tab is clicked")

            fp.justification_element().clear()
            if(justifyValue!=None):
                fp.justification_element().send_keys(justifyValue)
                logging.info("The justification is added")

            time.sleep(2)
            fp.scheduletab_element().click()
            logging.info("The schedule tab is clicked")

            fp.startdate_element().clear()
            start_date_val = datetime.now() + timedelta (minutes=20)
            start_date_formatted = start_date_val.strftime("%Y-%m-%d %H:%M:%S")
            fp.startdate_element().send_keys(start_date_formatted)
            logging.info("The start date is added")

            fp.enddate_element().clear()
            end_date_val = datetime.now() + timedelta (days=7)
            end_date_formatted = end_date_val.strftime("%Y-%m-%d %H:%M:%S")
            fp.enddate_element().send_keys(end_date_formatted)
            logging.info("The end date is added")

            time.sleep(2)
            fp.submit_element().click()
            print("The change is submitted")
            time.sleep(3)

            assert fp.shortdescription_element().get_attribute("value") != "", "Short description should not be empty"
            assert fp.description_element().get_attribute("value") != "", "Description should not be empty"
            assert fp.assignmentci_element().get_attribute("value") != "", "Assignment CI is invalid/empty"
            assert fp.assignmentgroup_element().get_attribute("value") != "", "Assignment group is invalid/empty"
            '''
            newChangeValue = fp.newchangerequest_element().get_attribute("value")
            logging.info(type(newChangeValue))
            if(newChangeValue!=""):
                logging.info("The value of new change request is sent: %s", newChangeValue)
                return newChangeValue
            else:
                logging.info("The new change request is not created")
                return None

        except NoSuchElementException:
            logging.info("There is no such element exception")
            return None

        except AssertionError as ae:

            logging.error(f'Assert Error: {ae}')
            return None

        except Exception as e:
            logging.error(f'An unexpected error occured: {e}')
            return None
