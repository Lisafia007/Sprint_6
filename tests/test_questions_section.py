import allure
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import QuestionsPageLocators
from pages import QuestionsPageScooter

class TestQuesctionsSection:

   driver = None

   @classmethod
   def setup_class(cls):
      cls.driver = webdriver.Firefox()
      cls.driver.get('https://qa-scooter.praktikum-services.ru/')

   @allure.title("Проверка выпадающего списка в разделе 'Вопросы о важном'")   
   @allure.description("Нажимаем на стрелочку и проверяем, что открывается соответствующий текст на каждый вопрос")
   @pytest.mark.parametrize("index", range(8))
   def test_text_check_after_click(self, index):

      self.driver.delete_all_cookies()
      self.driver.refresh()

      qustions_page = QuestionsPageScooter(self.driver)
      qustions_page.section()
             
      assert self.driver.find_element(*QuestionsPageLocators.QUESTIONS_SECTION).is_displayed()

      qustions_page.text_check_after_click(index)
      
      text_element = self.driver.find_element(*QuestionsPageLocators.TEXTS[index])

      assert text_element.is_displayed()

   @classmethod
   def teardown_class(cls):
      cls.driver.quit() 
