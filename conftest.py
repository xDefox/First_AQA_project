import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption(
        "--language",
        action="store",
        default="en",
        help="choose language: ru, en, es, uk, fr. Default language is en",
    )


@pytest.fixture(scope="function")
def browser(request):
    print("\nstart browser for test..")
    page_language = request.config.getoption("language")

    options = Options()
    options.add_argument(f"--lang={page_language}")

    browser = webdriver.Chrome(options=options)
    yield browser
    print("\nquit browser..")
    browser.quit()