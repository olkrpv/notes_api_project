# Сервис для публикации записей

### Описание
Данный проект представляет собой API-сервис для публикации записей, где пользователи могут создавать/редактировать/удалять свои посты, читать чужие, комментировать их, а также подписываться на других авторов.
Посты можно объединять в тематические группы.
Цель разработки проекта - глубже изучить Django Rest Framework и отточить создание REST API на типичном примере социальной сети.

### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone git@github.com:olkrpv/notes_api_project.git
```

```
cd notes_api_project
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv venv
```

```
source venv/bin/activate
```

Обновить pip:
```
python3 -m pip install --upgrade pip
```

Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

Перейти в папку Django-проекта:

```
cd yatube_api
```

Выполнить миграции:

```
python3 manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
```

### Документация API
После запуска проекта документация к API будет доступна по адресу:
http://127.0.0.1:8000/redoc/

### Стек технологий:
- Python 3.9
- Django Framework
- Django Rest Framework
- JWT+Djoser
