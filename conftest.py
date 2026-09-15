import pytest
from selenium import webdriver

#Драйвер
@pytest.fixture
def driver(request):
   driver = webdriver.Firefox()
   request.addfinalizer(driver.quit)
   return driver