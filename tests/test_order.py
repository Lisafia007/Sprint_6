import allure
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import OrderButtonLocators, BasePageLocators, LogoPageLocators
from pages import OrderButtonScooter, BasePageScooter, LogoPageScooter
from data.order_data import DATA_SET_1, DATA_SET_2

class TestOrder:

   driver = None

   @classmethod
   def setup_class(cls):
      cls.driver = webdriver.Firefox()


   def _form_data_order(self, button_locator, order_data):
      self.driver.delete_all_cookies()
      self.driver.get('https://qa-scooter.praktikum-services.ru/')

      order = OrderButtonScooter(self.driver)
      order.close_cookie()
      order.click_order_button(button_locator)
      order.filling_out_form(order_data)
      order.filling_about_renting(order_data)
      order.confirm_order()
      order.show_success_order()

      return order

   @allure.title("Проверка позитивного сценария заказа самоката")   
   @allure.description("Заполняем формы заказа самоката с двумя наборами данных и двумя точками входа соответственно")
   @pytest.mark.parametrize("button_locator, order_data", [
    (OrderButtonLocators.TOP_ORDER_BUTTON, DATA_SET_1),
    (OrderButtonLocators.BOTTOM_ORDER_BUTTON, DATA_SET_2),
   ])
   def test_order_success(self, button_locator, order_data):
      self._form_data_order(button_locator, order_data)   

      order_placed = self.driver.find_element(*BasePageLocators.ORDER_PLACED_WINDOW)
      assert order_placed.is_displayed()

   @allure.title("Проверка логотипа Самоката")   
   @allure.description("После успешного создания заказа нажимаем на логотип Самоката и переходим на главную страницу 'Самоката'")
   def test_logo_shooter(self):
      self._form_data_order(OrderButtonLocators.TOP_ORDER_BUTTON, DATA_SET_1)
      logo = LogoPageScooter(self.driver)
      logo.show_status()
      logo.go_to_logo_scooter()

      assert self.driver.current_url == "https://qa-scooter.praktikum-services.ru/"

   @allure.title("Проверка логотипа Яндекса")   
   @allure.description("После успешного создания заказа нажимаем на логотип Яндекса и в новом окне откроется главная страница Дзена")
   def test_logo_yandex(self):
      self._form_data_order(OrderButtonLocators.BOTTOM_ORDER_BUTTON, DATA_SET_2)
      logo = LogoPageScooter(self.driver)
      logo.show_status()

      windows_before = self.driver.window_handles
      logo.go_to_logo_yandex()

      WebDriverWait(self.driver, 10).until(expected_conditions.new_window_is_opened(windows_before)
    )
      self.driver.switch_to.window(self.driver.window_handles[1])

      WebDriverWait(self.driver, 15).until(expected_conditions.url_contains("dzen.ru"))
      assert "dzen.ru" in self.driver.current_url 



   @classmethod
   def teardown_class(cls):
      cls.driver.quit() 
