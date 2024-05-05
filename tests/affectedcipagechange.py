from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException 
from selenium.webdriver.support.select import Select
from webelementpage.affectedcipage import AffectedCIPage
import logging
import time

class Affectedcipagechange:

    def __init__(self, driver):
        self.driver = driver

    
    def affectedci_func(self, ACISheet, r):
        afci = AffectedCIPage(self.driver)
        time.sleep(3)
        afci.affectedcitab_element().click()
        logging.info("Affected CI tab is clicked")
        time.sleep(4)
        afci.affectedciedit_element().click()
        logging.info("Affected CI edit button is clicked")
        count = 0
        try:
            time.sleep(4)
            while(afci.removefilter_element()!=None):
                time.sleep(2)
                afci.removefilter_element().click()
                count = count+1
                logging.info("The filter is removed: %s", count)
        except:
            logging.info("All the filters has been removed")

        try: 
            time.sleep(3)
            selectcollectedCI = afci.collectedCI_element()
            logging.info("All the collected CI is selected")
            optioncollectedCI = Select(selectcollectedCI)
            logging.info("All options of the collected CI is selected")
            time.sleep(2)
            for option in optioncollectedCI.options:
                if(option.text!=ACISheet.cell(r,1).value):
                    time.sleep(2)
                    optioncollectedCI.select_by_visible_text(option.text)
                    logging.info("Apart from assignment ci others are removed")
                    time.sleep(2)
                    afci.removefromcollection_element().click()
                    logging.info("remove is clicked")
        except:
            logging.info("error")
        c = 2
        try:
            while(ACISheet.cell(r,c).value != None):
                time.sleep(3)
                searchCI = afci.searchCI_element()
                affectedCIval = ACISheet.cell(r,c).value
                affectedCIval = affectedCIval.strip()
                searchCI.clear()
                searchCI.send_keys(affectedCIval)
                logging.info("The affected CI has been searched")
                time.sleep(4)
                selectAffectedCI = afci.selectCI_element()
                logging.info("The Affected CI select element is called")
                optionAffectedCI = Select(selectAffectedCI)
                logging.info("The Affected CI select element is loaded")
                time.sleep(5)
                optionAffectedCI.select_by_visible_text(affectedCIval)
                logging.info("The affected CI has been clicked from option")
                afci.addtocollection_element().click()
                logging.info("The affected CI has been added to the collection")
                c=c+1
            time.sleep(2)
            afci.save_element().click()
            logging.info("All affected CI has been saved to the collection")
            time.sleep(2) 
        except Exception as e: 
            logging.error(f'An unexpected error occured: {e}')
            

        
