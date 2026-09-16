import allure
import pytest
from locators import OrderButtonLocators, BasePageLocators, LogoPageLocators
from pages import OrderButtonScooter, BasePageScooter, LogoPageScooter
from data import DATA_SET_1, DATA_SET_2, URLS

class TestOrder:
   def _form_data_order(self, driver, button_locator, order_data):
      order = OrderButtonScooter(driver)
      order.delete_cookies()
      order.open(URLS.BASE_URL)

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
   def test_order_success(self, driver, button_locator, order_data):
      order = self._form_data_order(driver, button_locator, order_data)   
      
      assert order.is_element_displayed(BasePageLocators.ORDER_PLACED_WINDOW)

   @allure.title("Проверка логотипа Самоката")   
   @allure.description("После успешного создания заказа нажимаем на логотип Самоката и переходим на главную страницу 'Самоката'")
   def test_logo_shooter(self, driver):
      self._form_data_order(driver, OrderButtonLocators.TOP_ORDER_BUTTON, DATA_SET_1)
      logo = LogoPageScooter(driver)
      logo.show_status()
      logo.go_to_logo_scooter()

      assert URLS.SCOOTER_MAIN_URL in logo.get_current_url() 

   @allure.title("Проверка логотипа Яндекса")   
   @allure.description("После успешного создания заказа нажимаем на логотип Яндекса и в новом окне откроется главная страница Дзена")
   def test_logo_yandex(self, driver):
      self._form_data_order(driver, OrderButtonLocators.BOTTOM_ORDER_BUTTON, DATA_SET_2)
      logo = LogoPageScooter(driver)
      logo.show_status()

      windows_before = logo.get_window_handles()
      logo.go_to_logo_yandex()
      logo.switch_to_new_window(windows_before)

      logo.wait_url_contains("dzen.ru")
      assert "dzen.ru" in logo.get_current_url()
