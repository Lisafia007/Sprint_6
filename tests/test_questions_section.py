import allure
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import QuestionsPageLocators
from pages import QuestionsPageScooter, BasePageScooter 
from data import URLS

class TestQuesctionsSection:


   @allure.title("Проверка выпадающего списка в разделе 'Вопросы о важном'")   
   @allure.description("Нажимаем на стрелочку и проверяем, что открывается соответствующий текст на каждый вопрос")
   @pytest.mark.parametrize("index", range(8))
   def test_text_check_after_click(self, driver, index):

      qustions_page = QuestionsPageScooter(driver)
      qustions_page.delete_cookies()
      qustions_page.open(URLS.BASE_URL)
      qustions_page.refresh()
      qustions_page.section()
             
      assert qustions_page.is_element_displayed(QuestionsPageLocators.QUESTIONS_SECTION)

      qustions_page.text_check_after_click(index)
      
      assert qustions_page.is_element_displayed(QuestionsPageLocators.TEXTS[index])

