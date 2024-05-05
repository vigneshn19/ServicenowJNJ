from selenium import webdriver 
import pytest

@pytest.fixture()
def test_initial_setup(request):
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach",True)
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.delete_all_cookies()
    request.cls.driver = driver
    yield
    driver.quit()