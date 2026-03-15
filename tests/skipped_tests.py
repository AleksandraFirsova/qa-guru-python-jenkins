from selene.support.shared import browser
from selene import have, be


@pytest.mark.skip(reason="Временно пропускаем")
def test_example_title_success():
    browser.open('https://example.com')
    assert browser.driver.title == 'Example Domain'


@pytest.mark.skip(reason="Временно пропускаем")
def test_example_h1_success():
    browser.open('https://example.com')
    browser.element('h1').should(have.text('Example Domain'))


@pytest.mark.skip(reason="Временно пропускаем")
def test_example_element_visible():
    browser.open('https://example.com')
    browser.element('p').should(be.visible)


@pytest.mark.skip(reason="Временно пропускаем")
def test_example_url_check():
    browser.open('https://example.com')
    assert browser.driver.current_url == 'https://example.com/'