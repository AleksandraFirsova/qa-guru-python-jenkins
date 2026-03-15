from selene import browser
from selene import have, be


def test_example_title_success():
    browser.open('/')
    assert browser.driver.title == 'Example Domain'


def test_example_h1_success():
    browser.open('/')
    browser.element('h1').should(have.text('Example Domain'))


def test_example_element_visible():
    browser.open('/')
    browser.element('p').should(be.visible)


def test_example_url_check():
    browser.open('/')
    assert browser.driver.current_url == 'https://example.com/'
