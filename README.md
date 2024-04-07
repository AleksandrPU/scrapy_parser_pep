# Проект асинхронного парсинга PEP

## Описание:

Учебный проект по изучению асинхронного парсинга сайтов с помощью фреймворка 
[Scrapy](https://scrapy.org/).

Программа предназначена для получения информации о Python PEP с сайта 
[peps.python.org](https://peps.python.org):

- список PEP со статусами;

- количество PEP по статусам.

Информация выводится в формате csv в каталог results:

- pep_<дата в формате ISO>.csv

- status_summary_<дата в формате ISO>.csv

## Использование:

1. Склонировать проект:

```
git clone git@github.com:AleksandrPU/scrapy_parser_pep.git
```

2. Перейти в директорию склонированного проекта:

```
cd scrapy_parser_pep
```

3. Создать виртуальное окружение:

```
python3.9 -m venv venv
```

**ВНИМАНИЕ!** Необходимо использовать Python версии 3.9.

4. Активировать виртуальное окружение:

```
source venv/bin/activate
```

5. Установить зависимости:

```
pip install -r requirements.txt
```

6. Запуск парсера:

```
scrapy crawl pep
```

## Автор:

Проект создан Паутовым Александром на основе репозитория 
[yandex-praktikum/scrapy_parser_pep](https://github.com/yandex-praktikum/scrapy_parser_pep)
