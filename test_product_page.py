import pytest

from pages.product_page import ProductPage
import time

@pytest.mark.parametrize('promo_code', [0, 1, 2, 3, 4, 5, 6,
                                  pytest.param('7', marks=pytest.mark.xfail),
                                  range(8, 9)])
def test_guest_can_add_product_to_basket(browser, promo_code):
    link = ('http://selenium1py.pythonanywhere.com/catalogue/'
                   'coders-at-work_207/?promo=offer{}'.format(promo_code))
    page = ProductPage(browser, link)
    page.open()
    page.guest_can_add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_the_same_product()
    page.should_be_the_same_price()
