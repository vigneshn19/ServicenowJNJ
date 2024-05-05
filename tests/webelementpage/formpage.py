from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
import time

class FormPage:

    copychangebutton = '//*[@id="copy_change_request"]'
    urgency = '//*[@id="change_request.urgency"]'
    shortdescription = '//*[@id="change_request.short_description"]'
    description = '//*[@id="change_request.description"]'
    assignmentci = '//*[@id="sys_display.change_request.cmdb_ci"]'
    assignmentgroup = '//*[@id="sys_display.change_request.assignment_group"]'
    planningtab = '//*[@id="tabs2_section"]/span[1]/span[1]/span[2]'
    justification = '//*[@id="change_request.justification"]'
    scheduletab = '//*[@id="tabs2_section"]/span[3]/span[1]'
    startdate = '//*[@id="change_request.start_date"]'
    enddate = '//*[@id="change_request.end_date"]'
    submit = '//*[@id="sysverb_update_and_stay"]'
    newchangerequest = '//*[@id="sys_readonly.change_request.number"]'
    dismiss = '//*[@id="special_handling_notes_closemodal"]'

    def __init__(self, driver):
        self.driver = driver

    def formshadowroot_element(self):
        shadow_root1 = self.driver.find_element(By.CSS_SELECTOR,'body > macroponent-f51912f4c700201072b211d4d8c26010[app-id="a84adaf4c700201072b211d4d8c260b7"]').shadow_root
        return shadow_root1

    def leaveshadowroot_element(self):
        shadow_root2 = self.formshadowroot_element().find_element(By.CSS_SELECTOR,'div > sn-canvas-appshell-root > sn-canvas-appshell-layout > sn-polaris-layout').shadow_root
        shadow_root3 = shadow_root2.find_element(By.CSS_SELECTOR,'div.sn-polaris-layout.polaris-enabled > div.layout-main > div.content-area.is-pinned.can-animate > now-modal.dirty-form-confirmation').shadow_root
        shadow_root4 = shadow_root3.find_element(By.CSS_SELECTOR, 'div > div > div > div.now-modal-footer > now-button.now-modal-footer-button+now-button.now-modal-footer-button').shadow_root
        return shadow_root4

    def iframe_element(self):
        iframe = self.formshadowroot_element().find_element(By.CSS_SELECTOR, 'div > sn-canvas-appshell-root > sn-canvas-appshell-layout > sn-polaris-layout > iframe[id="gsft_main"]')
        return iframe

    def leavebutton_element(self):
        time.sleep(3)
        leavebutton = self.leaveshadowroot_element().find_element(By.CSS_SELECTOR,'button')
        return leavebutton

    def copychangebutton_element(self):
        return self.driver.find_element(By.XPATH,self.copychangebutton)

    def urgency_element(self):
        return self.driver.find_element(By.XPATH,self.urgency)
    
    def shortdescription_element(self):
        return self.driver.find_element(By.XPATH, self.shortdescription)    
    
    def description_element(self):
        return self.driver.find_element(By.XPATH,self.description)

    def assignmentci_element(self):
        return self.driver.find_element(By.XPATH,self.assignmentci)

    def assignmentgroup_element(self):
        return self.driver.find_element(By.XPATH, self.assignmentgroup)

    def planningtab_element(self):
        return self.driver.find_element(By.XPATH,self.planningtab)
    
    def justification_element(self):
        return self.driver.find_element(By.XPATH,self.justification)

    def scheduletab_element(self):
        return self.driver.find_element(By.XPATH,self.scheduletab)
    
    def startdate_element(self):
        return self.driver.find_element(By.XPATH, self.startdate)

    def enddate_element(self):
        return self.driver.find_element(By.XPATH, self.enddate)

    def submit_element(self):
        return self.driver.find_element(By.XPATH, self.submit)

    def newchangerequest_element(self):
        return self.driver.find_element(By.XPATH, self.newchangerequest)

    def dismiss_element(self):
        return self.driver.find_element(By.XPATH, self.dismiss)
        
