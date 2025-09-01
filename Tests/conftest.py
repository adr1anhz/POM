import pytest
from selenium import webdriver

@pytest.fixture(params=["chrome", "firefox"], scope='class')
def init_driver(request):
    if request.param == "chrome":
        web_driver = webdriver.Chrome()  # automatycznie używa chromedriver z PATH
    elif request.param == "firefox":
        web_driver = webdriver.Firefox()  # automatycznie używa geckodriver z PATH
    
    request.cls.driver = web_driver
    web_driver.implicitly_wait(10)
    
    yield
    web_driver.quit()
