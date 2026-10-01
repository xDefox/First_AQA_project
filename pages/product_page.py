from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_product_to_cart(self):
        add_button = self.browser.find_element(*ProductPageLocators.CART_BUTTON)
        add_button.click()

    def solve_quiz(self):
        self.solve_quiz_and_get_code()

    def should_be_confirm_message(self):
        assert self.is_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is not presented"

    def name_should_be_product_name(self):
        name_of_product = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        book_alert_text = self.browser.find_element(*ProductPageLocators.ALERT_WITH_BOOK_NAME)
        assert name_of_product.text == book_alert_text.text, \
            "Product name in the message does not match the added product"

    def should_be_true_summ_in_the_cart(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        basket_price = self.browser.find_element(*ProductPageLocators.BASKET_PRICE_MESSAGE)
        assert product_price.text == basket_price.text, \
            "Basket price does not match product price"