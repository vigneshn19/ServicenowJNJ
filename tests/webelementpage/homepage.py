from selenium.webdriver.common.by import By

class HomePage:

    remindmeLater = 'body > div.modal.fade.ng-isolate-scope.in > div > div > div > div.panel-footer.loc-set-footer > div.action-button-container > a.ng-scope'
    closebutton = 'body > div.modal.fade.ng-isolate-scope.in > div > div > div > div.panel-footer.loc-set-footer > div.close-modal-btn > button.btn.btn-primary.ng-scope'
    itsm = '//*[@id="itsm"]/span'

    def __init__(self, driver):
        self.driver = driver

    def remindmelater_element(self):
        return self.driver.find_element(By.CSS_SELECTOR, self.remindmeLater)

    def closebutton_element(self):
        return self.driver.find_element(By.CSS_SELECTOR, self.closebutton)

    def itsm_element(self):
        return self.driver.find_element(By.XPATH, self.itsm)