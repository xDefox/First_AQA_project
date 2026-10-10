# First_AQA_project

Учебный проект по автоматизации тестирования (курс Stepik "Автоматизация тестирования с помощью Selenium и Python").

## Что внутри

Автотесты на [учебный сайт](http://selenium1py.pythonanywhere.com) построены по паттерну **Page Object**:

```
pages/
  base_page.py      # базовые действия (open, ожидания, проверки элементов)
  locators.py       # все локаторы вынесены отдельно от логики
  main_page.py      # главная страница
  login_page.py     # страница логина
  product_page.py   # страница товара
conftest.py         # фикстура browser + опция --language
test_main_page.py
test_product_page.py
```

## Стек

- Python 3
- Selenium WebDriver
- pytest

## Запуск

```bash
pip install selenium pytest
pytest --language=ru
```

Язык интерфейса задаётся опцией `--language` (`ru`, `en`, `es`, `uk`, `fr`), по умолчанию `en`.

> Для запуска нужен установленный Chrome и chromedriver в `PATH`.
