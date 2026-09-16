import allure
from pages.base_page import BasePageScooter


class OrderButtonScooter(BasePageScooter):

   #Метод нажатия на кнопку "Заказать"
   @allure.step("Нажимаем на кнопку 'Заказать'")
   def click_order_button(self, locator):
      self.wait_element_to_be_clickable(locator).click()