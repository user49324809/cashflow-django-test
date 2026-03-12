# CashFlow Test Task

Веб-приложение для учета движения денежных средств (ДДС), разработанное на Django.

## Функциональность

* Создание записи о движении денежных средств
* Редактирование записей
* Удаление записей
* Просмотр списка операций
* Фильтрация по:

  * дате
  * статусу
  * типу
  * категории
  * подкатегории
* Управление справочниками через Django Admin
* Динамическая зависимость:

  * Тип → Категория → Подкатегория

## Технологии

* Python
* Django
* SQLite
* Bootstrap
* JavaScript (AJAX)
* Django ORM
* django-filter

## Установка

Склонировать репозиторий:

git clone [https://github.com/user49324809/cashflow-test.git](https://github.com/user49324809/cashflow-test.git)

Перейти в папку проекта:

cd cashflow-test

Создать виртуальное окружение:

python -m venv venv

Активировать окружение:

Windows:
venv\Scripts\activate

Mac/Linux:
source venv/bin/activate

Установить зависимости:

pip install -r requirements.txt

## Настройка базы данных

Выполнить миграции:

python manage.py migrate

Создать администратора:

python manage.py createsuperuser

## Запуск проекта

python manage.py runserver

Открыть в браузере:

[http://127.0.0.1:8000](http://127.0.0.1:8000)

Админ панель:

[http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin)