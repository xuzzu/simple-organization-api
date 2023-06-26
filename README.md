# DRF Test Project
Этот проект представляет собой API для управления организацией. Он написан на Python 3.8 с использованием Django REST Framework, в качестве СУБД использовалась PostgreSQL

## Установка
Для работы с этим проектом необходимо установить Python версии 3.8 в чистую виртуальную среду (я использовал Miniconda для мэнеджмента сред) и выполнить следующие шаги:

Склонировать репозиторий с помощью
```
git clone https://github.com/xuzzu/simple-organization-api.git
```
Перейти в папку проекта и установить все зависимости из requirements.txt
```
cd django_test_app
pip install -r requirements.txt
```
Опционально - загрузить файл датабазы в PostgreSQL на локальном хосте со стандартным портом 5432, используя PgAdmin 4.
Выполнить необходимые миграции ДБ:
```
python manage.py makemigrations
python manage.py migrate
```
## Использование
API доступно по адресу /api/, а административная панель - по адресу /admin/. Документация Swagger UI доступна по адресу /docs/.

## Проект включает следующие модели:

Person - информация о работнике (поле для фотографии оставил обычным байтфилдом)

Department - информация о депортаменте / подразделении

Position - информация о должности

Task - информация о задании и дедлайне

PersonTask - бридж таблица для моделей Person и Task


## Помимо стандартных представлений для моделей выше, сделаны следующие:

OrganizationStructureView - для построения дерева организации

PersonSummaryView - для отображения информации в профиле пользователя

### API также включает функцию для рассылки уведомлений на email в папке management.

## Тестирование
Проект содержит некоторе покрытие unit-тестами и нагрузочные тесты для некоторых операций, которые можно запустить с помощью Locust.
```
cd django_test_app
locust -f load_tests.py --headless -u 100 -r 10 --run-time 1m   
```
## Комментарии*

- Пара логин:пароль для загруженной мною ДБ admin:admin
- Модели наследующие от MPTT имеют дополнительные скрытые поля для построения дерева, которые должны быть не NULL. Я не стал запускать автоматическое перестроение в миграции и при добавлении новых записей ставлю стандартное значение = 0
- Схема базы данных:
  
  ![alt text](schema.png)
